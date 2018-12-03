
from rest_framework.views import APIView
from rest_framework.response import Response
from django_redis import get_redis_connection
from django.conf import settings
import json

from app01 import models
class ShoppingCarView(APIView):
    redis_conn = get_redis_connection()
    cache_key = settings.CACHE_KEY
    def get(self, request, *args, **kwargs):
        user_id = request.auth.user.id
        key = self.cache_key%(user_id, '*')
        buy_car = []
        for item in self.redis_conn.scan_item(key):
            self.redis_conn.hgetall(item)
            buy_car.append({

            })

        return Response("ok")

    def post(self, request, *args, **kwargs):
        '''
        添加商品到购物车
        {
            "account_id":1,
            "course_id":5,
            "policy_id":5
        }
        :param args:
        :param kwargs:
        :return:
        '''
        #写入redis重新生成一个key，写入前先验证合法性
        print('auth==>', request.auth)
        user_id = request.auth.user.id
        course_id = request.data.get("course_id")
        policy_id = request.data.get("policy_id")
        #验证课程合法性
        course_obj = models.Course.objects.get(id=course_id) #没有时处理异常跑错
        #验证价格策略合法性
        policy_dict = {}
        for item in course_obj.price_policy.all():
            policy_dict[item.id] = {
                "valid_period":item.get_valid_period_display(),
                "price":item.price,
            }

        if policy_id not in policy_dict:
            print('不合法')  #抛出异常

        add_data = {
            "title":course_obj.name,
            "course_img":course_obj.course_img,
            "price_policy":policy_dict,
            "default_policy":policy_id
        }
        #写入redis
        self.redis_conn.hmset(self.cache_key%(user_id, course_id), add_data)
        return Response('ok')

    def put(self, request, *args, **kwargs):
        #修改价格策略  也要验证合法性
        user_id = request.auth.user.id
        course_id = request.data.get('course_id')
        policy_id = request.data.get('policy_id')
        key = self.cache_key%(user_id, course_id)
        if not self.redis_conn.exists(key):
            print('课程不存在')
        policy_dict = json.loads(self.redis_conn.hget(key, 'price_policy'))
        if str(policy_id) not in policy_dict:
            print('存在此价格策略')

        self.redis_conn.set(key, 'default_policy', policy_id)
        return Response('ok')

    def delete(self, request, *args, **kwargs):
        # 清除课程key前，先验证课程id合法性
        course_id = request.data.get('course_id')
        key = self.cache_key%(request.auth.user.id, course_id)
        if not self.redis_conn.exists(key):
            print('没有此课程')
        self.conn.delete(key)
        return Response('ok')
