# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import datetime
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django_redis import get_redis_connection
from django.db.models import Q

from app01.utils.response import BaseResponse
from app01.utils.data_valid_errors import CourseInvalid, CouponInvalid
from app01 import models

'''
结算时写入redis的数据结构：
    主要是两块：课程信息和优惠券信息
    1.课程信息：
        标题，图片，有效期，价格
    2.优惠券：
        课程优惠券 优惠券id，类型，编号，使用状态，课程ID
        全局优惠券 优惠券id，类型，编号，使用状态，课程ID 0
    
    {
        "payment_用户ID_coupon_券ID"：{
            优惠券id：1，
            类型：通用券，
            编号：2，
            使用状态：未使用，
            满减多少，折扣多少...
            课程ID：2  #全局默认为0
        }，
        payment_用户ID_course_课程ID:{
            标题，图片，策略ID, 有效期，价格，优惠券字典，默认优惠券ID(默认为0)
        }
        从redis获取课程显示，优惠券是个字典，
            那写入时有两种情况：一个是给个优惠券id列表，如果这里给了id，下次获取时，只要拼接key就能获取想要的优惠券
                    一个是不给，下次获取时，循环所有的优惠券 根据课程ID值判断
            
        
        payment_global_coupon_用户ID:6
    }
    
    post添加到去结算：
        把发送的课程全部添加到redis中，
            (根绝购物车redis判断课程是否合法)
            (然后把购物车redis课程数据添加到结算redis中)
        根据用户把所有的可用优惠券添加到redis中
            (去数据库中获取写入-未使用，有效时间范围内)
        
    get所有结算商品和优惠券
        根据用户 * 匹配模式
    
    patch修改优惠券
        课程优惠券修改：根据用户和课程 修改优惠券ID
        全局优惠券：修改pay_bill_用户ID_global_coupon_id
'''

class PayBillView(APIView):
    redis_conn = get_redis_connection()
    def post(self, request, *args, **kwargs):
        '''去结算，把结算商品和优惠券写入redis {course_ids:[1,2]}'''
        ret = BaseResponse()
        try:
            user_id = request.auth.user_id

            #添加前，先清空当前用户所有商品
            course_match = settings.PAYMENT_COURSE_KEY %(user_id, '*', )
            coupon_match = settings.PAYMENT_COUPON_KEY %(user_id, '*', )
            global_coupon_match = settings.PAYMENT_GLOBAL_COUPON_KEY %(user_id, )
            for key_match in [course_match, coupon_match, global_coupon_match]:
                for key in self.redis_conn.scan_iter(key_match):
                    self.redis_conn.delete(key)

            course_ids = request.data.get("course_ids")
            #判断是否课程合法性
            buy_car_course_keys = [settings.CACHE_KEY %(user_id, course_id,) for course_id in course_ids]
            course_exist_list = [self.redis_conn.exists(key) for key in buy_car_course_keys]
            if not all(course_exist_list):
                raise CourseInvalid("课程在购物车中不存在")

            #获取用户所有能用的优惠券
            q1 = Q(status=0) # 未使用
            now_date = datetime.date.today()
            q2 = Q(coupon__valid_begin_date__lte=now_date) & Q(coupon__valid_end_date__gte=now_date)  # 有效时间范围内
            q3 = Q(account=user_id) #当前用户
            coupons = models.CouponRecord.objects.filter(q1&q2&q3)

            #把优惠券写入redis中
            for coupon in coupons:
                if str(coupon.coupon.object_id) in [str(course_int) for course_int in course_ids] or \
                    not coupon.coupon.object_id:
                    coupon_key = settings.PAYMENT_COUPON_KEY %(user_id, coupon.id,)
                    coupon_dict = {
                        'id': coupon.id,
                        'coupon_type':coupon.coupon.get_coupon_type_display(),
                        'number':coupon.number,
                        'status':coupon.status,
                        'course_id':coupon.coupon.object_id or 0
                    }

                    #判断券类型  获取   满减多少，折扣多少...
                    if coupon.coupon.coupon_type == 0: #通用券
                        coupon_dict['money_equivalent_value'] = coupon.coupon.money_equivalent_value
                    elif coupon.coupon.coupon_type == 1: #满减券
                        coupon_dict['money_equivalent_value'] = coupon.coupon.money_equivalent_value
                        coupon_dict['minimum_consume'] = coupon.coupon.minimum_consume
                    elif coupon.coupon.coupon_type == 2: #折扣券
                        coupon_dict['minimum_consume'] = coupon.coupon.off_percent
                    self.redis_conn.hmset(coupon_key, coupon_dict)

            #把课程写入redis
            for course_id in course_ids:
                buy_car_key = settings.CACHE_KEY %(user_id, course_id,)
                payment_course_key = settings.PAYMENT_COURSE_KEY %(user_id, course_id)
                course_dict = {
                    'id': course_id,
                    'title': self.redis_conn.hget(buy_car_key, 'title'),
                    'course_img': self.redis_conn.hget(buy_car_key, 'course_img'),
                }

                default_policy = self.redis_conn.hget(buy_car_key, 'default_policy').decode('utf-8')
                policy_dict = json.loads(self.redis_conn.hget(buy_car_key, 'price_policy'))[default_policy]
                course_dict.update(policy_dict)
                course_dict['policy_id'] = default_policy

                course_dict['coupon_id'] = 0
                self.redis_conn.hmset(payment_course_key, course_dict)

            #设置默认全局优惠券
            global_coupon_key = settings.PAYMENT_GLOBAL_COUPON_KEY %(user_id, )
            self.redis_conn.set(global_coupon_key, 0)

            ret.data = course_ids
        except CourseInvalid as e:
            ret.code = 1001
            ret.error = e.msg
        except Exception as e:
            print(e)
            ret.code = 2001
            ret.error = "去结算课程失败"

        return Response(ret.dict)


    def patch(self, request, *args, **kwargs):
        '''修改优惠券，包括课程的和所有的
          {
            "course_id":0,
            "coupon_id":3
        }
            course_id为0时，就是全局优惠券
        '''
        ret = BaseResponse()
        try:
            user_id = request.auth.user_id
            course_id = str(request.data.get("course_id"))
            coupon_id = str(request.data.get("coupon_id"))

            #判断课程合法性
            #分为 无值  0  非0数字
            if course_id != '0':
                course_key = settings.PAYMENT_COURSE_KEY %(user_id, course_id)
                if not self.redis_conn.exists(course_key):
                    raise CourseInvalid("课程不存在")

            #判断优惠券合法性
            if coupon_id != '0':
                coupon_key = settings.PAYMENT_COUPON_KEY %(user_id, coupon_id)
                if not self.redis_conn.exists(coupon_key):
                    if course_id == '0':
                        raise CouponInvalid('全局优惠券不存在')
                    raise CouponInvalid("课程优惠券不存在")
                else:
                    coupon_course_id = self.redis_conn.hget(coupon_key, "course_id").decode('utf-8')
                    if course_id != coupon_course_id:
                        raise CouponInvalid('优惠券不合法')

            #优惠券修改
            global_coupon_id = settings.PAYMENT_GLOBAL_COUPON_KEY % (request.auth.user_id,)
            if course_id == "0": #全局优惠券
                self.redis_conn.set(global_coupon_id, coupon_id)
            else:
                course_key = settings.PAYMENT_COURSE_KEY % (user_id, course_id)
                self.redis_conn.hset(course_key, 'coupon_id', coupon_id)
            ret.data = "修改优惠券成功"

        except CourseInvalid as e:
            ret.code = 1001
            ret.error = e.msg
        except CouponInvalid as e:
            ret.code = 5001
            ret.error = e.msg
        except Exception as e:
            ret.code = 2001
            ret.error = "修改优惠券失败"

        return Response(ret.dict)

    def get(self, request, *args, **kwargs):
        '''查看结算商品'''
        try:
            ret = BaseResponse()
            user_id = request.auth.user_id

            payment = {}
            #获取所有的优惠券
            coupon_match = settings.PAYMENT_COUPON_KEY %(user_id, '*',)
            coupon_keys = self.redis_conn.scan_iter(coupon_match)
            coupons = []
            for coupon_key in coupon_keys:
                coupon_dict = {}
                coupon_items = self.redis_conn.hgetall(coupon_key)
                for k,v in coupon_items.items():
                    coupon_dict[k.decode('utf-8')] = v.decode('utf-8')
                coupons.append(coupon_dict)

            #获取所有的课程
            course_match = settings.PAYMENT_COURSE_KEY %(user_id, '*')
            course_keys = self.redis_conn.scan_iter(course_match)
            course_list = []
            for course_key in course_keys:
                course_id = self.redis_conn.hget(course_key, 'id').decode('utf-8')
                course_dict = {
                    'id': course_id,
                    'title': self.redis_conn.hget(course_key, 'title'),
                    'course_img': self.redis_conn.hget(course_key, 'course_img'),
                    "policy_id": self.redis_conn.hget(course_key, 'policy_id'),
                    "valid_period": self.redis_conn.hget(course_key, 'valid_period'),
                    "price": self.redis_conn.hget(course_key, 'price'),
                    'coupon_list': list(filter(lambda item: item['course_id'] == course_id, coupons)),
                    'coupon_id':self.redis_conn.hget(course_key, 'coupon_id'),
                }
                course_list.append(course_dict)
            payment['course_list'] = course_list

            payment['global_coupon_list'] = list(filter(lambda item: item['course_id'] == '0', coupons))
            global_coupon_key = settings.PAYMENT_GLOBAL_COUPON_KEY % (user_id,)
            payment['default_global_coupon_id'] = self.redis_conn.get(global_coupon_key)

            ret.data = payment
        except Exception as e:
            ret.code = 3001
            ret.error = "获取结算商品失败"

        return Response(ret.dict)