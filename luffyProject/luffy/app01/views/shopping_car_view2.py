
from rest_framework.views import APIView
from rest_framework.response import Response
from django_redis import get_redis_connection
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import json

from app01 import models
from app01.utils.response import BaseResponse
from app01.utils.data_valid_errors import PricePolicyInvalid, CourseInvalid

class ShoppingCarView(APIView):
    redis_conn = get_redis_connection()
    cache_key = settings.CACHE_KEY

    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            user_id = request.auth.user_id
            key = self.cache_key%(user_id, '*')
            buy_car = []
            for item in self.redis_conn.scan_iter(key, count=10):
                #hgetall 键值都为字节，取值要注意
                # hash_item = self.redis_conn.hgetall(item)
                # buy_car.append({
                #     "title": hash_item[b'title'],
                #     "course_img": hash_item[b'course_img'],
                #     "price_policy": json.loads(hash_item[b'price_policy']),
                #     "default_policy": hash_item[b'default_policy'],
                # })

                buy_car.append({
                    'title': self.redis_conn.hget(item, 'title'),
                    'course_img': self.redis_conn.hget(item, 'course_img'),
                    'price_policy': json.loads(self.redis_conn.hget(item, 'price_policy')),
                    'default_policy': self.redis_conn.hget(item, 'default_policy')
                })
            ret.data = buy_car
        except Exception as e:
            ret.code = 2001
            ret.error = "获取课程失败"
        return Response(ret.dict)

    def post(self, request, *args, **kwargs):
        '''
        添加商品到购物车
        {
            "course_id":5,
            "policy_id":5
        }
        :param args:
        :param kwargs:
        :return:
        '''
        ret = BaseResponse()

        #写入redis重新生成一个key，写入前先验证合法性
        user_id = request.auth.user_id
        course_id = request.data.get("course_id")
        policy_id = request.data.get("policy_id")
        try:
            #验证课程合法性
            course_obj = models.Course.objects.get(id=course_id)
            #验证价格策略合法性
            policy_dict = {}
            for item in course_obj.price_policy.all():
                policy_dict[item.id] = {
                    "valid_period":item.get_valid_period_display(),
                    "price":item.price,
                }

            if policy_id not in policy_dict:
                raise PricePolicyInvalid("价格策略不合法")

            add_data = {
                "title": course_obj.name,
                "course_img": course_obj.course_img,
                "price_policy": json.dumps(policy_dict),
                "default_policy": policy_id
            }
            #写入redis
            self.redis_conn.hmset(self.cache_key%(user_id, course_id), add_data)
            ret.data = add_data
        except ObjectDoesNotExist as e:
            ret.code = 1002
            ret.error = "课程不存在"
        except PricePolicyInvalid as e:
            ret.code = 1003
            ret.error = e.msg
        except Exception as e:
            print(e)
            ret.code = 1004
            ret.error = "添加购物车失败"
        return Response(ret.dict)

    def put(self, request, *args, **kwargs):
        '''
        {
            "course_id": 5,
            "policy_id": 4
        }
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = BaseResponse()
        try:
            #修改价格策略  也要验证合法性
            user_id = request.auth.user_id
            course_id = request.data.get('course_id')
            policy_id = request.data.get('policy_id')
            key = self.cache_key%(user_id, course_id)
            if not self.redis_conn.exists(key):
                raise CourseInvalid("课程不存在")
            policy_dict = json.loads(self.redis_conn.hget(key, 'price_policy'))
            if str(policy_id) not in policy_dict:
                raise PricePolicyInvalid("不存在存在此价格策略")
            self.redis_conn.hset(key, 'default_policy', policy_id)
            ret.data = {"default_policy":policy_id}
        except CourseInvalid as e:
            ret.code = 3001
            ret.error = e.msg
        except PricePolicyInvalid as e:
            ret.code = 2001
            ret.error = e.msg
        except Exception as e:
            ret.code = 4001
            ret.error = "修改价格策略失败"
        return Response(ret.dict)

    def delete(self, request, *args, **kwargs):
        '''
        支持批量删除
        {
            "course_ids":[5,6]
        }
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = BaseResponse()
        try:
            # 清除课程key前，先验证课程id合法性
            course_ids = request.data.get('course_ids')
            keys = [self.cache_key%(request.auth.user_id, course_id) for course_id in course_ids]
            not_exist_keys = filter(lambda k:not self.redis_conn.exists(k), keys)
            if list(not_exist_keys):
                raise CourseInvalid("不存在此课程")
            self.redis_conn.delete(*keys)
            ret.data = {}
        except CourseInvalid as e:
            ret.code = 1002
            ret.error = e.msg
        except Exception as e:
            print(e)
            ret.code = 3001
            ret.error = "删除课程失败"
        return Response(ret.dict)
