# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from django_redis import get_redis_connection
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
import json

from app01 import serializer
from app01 import models

'''
购物车保存redis：
    临时状态
    频繁更新购物信息
'''

'''
购物车在redis中存储结构：
    shopping_car:{
        用户ID:{
            课程ID:{
                title:"金融量化"，
                img："/xx/xx.png",
                policy:{
                    价格策略ID:{"name":"有效期1个月"，"price":599},
                    价格策略ID:{"name":"有效期3个月"，"price":1299},
                },
                default_policy:xx_id
            },
            课程ID:{
                title:"金融量化"，
                img："/xx/xx.png",
                policy:{
                    价格策略ID:{"name":"有效期1个月"，"price":599},
                    价格策略ID:{"name":"有效期3个月"，"price":1299},
                },
                default_policy:xx_id
            }
        }
    }
'''

'''
业务分析：
    1.添加到购物车，post请求
        请求体 课程ID， 选中的价格策略ID
        从数据库获取课程详细，并判断价格策略合法性，写入redis
    
    2.查看购物车所有商品，get请求
        用户id
    
    3.购物车删除选中商品，delete请求
        用户id
        课程id(支持批量，是个列表)
    
    4.修改购物车，主要就是跟新价格策略， put/patch请求
        用户id
        课程id
        策略id
'''

class ShoppingCar(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        '''
        添加到购物车
        :param args:
        :param kwargs:
        :return:
        '''
        print(request.data)
        ss = serializer.ShoppingCarAddSerializers(data=request.data, many=False)
        print(ss.couse_id)
        print(type(ss.policy_id))
        if ss.is_valid():
            #验证价格合法性
            course_obj = models.Course.objects.filter(id=ss.couse_id).first()
            price_policy_list = course_obj.price_policy.all()
            filter_result = filter(lambda item: item.id == ss.policy_id, price_policy_list)
            if list(filter_result):
                #写入redis
                ass = serializer.ShoppingCarShowSerializers(instance=course_obj, many=False)
                ass.data['default_policy'] = ss.policy_id
                redis_conn = get_redis_connection()
                #先把用户之前的购物车数据取出来
                old_car = redis_conn.hget('shopping_car', ss.account_id)  #没有时 是不是空
                if old_car:
                    old_car = json.loads(old_car)
                else:
                    old_car = {}
                old_car[ss.couse_id] = ass.data
                redis_conn.hset('shopping_car', ss.account_id, json.dumps(old_car))
                return Response(ss.data)
            else:
                return Response('price policy id is error')
        else:
            return Response(ss.errors)

    def get(self, request, *args, **kwargs):
        '''
        查看购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        account_id = request.data.get('account_id')
        print(type(account_id))
        conn = get_redis_connection()
        course_dict_str = conn.hget('shopping_car',account_id)
        course_dict = json.loads(course_dict_str)
        return Response(course_dict)

    def delete(self, request, *args, **kwargs):
        '''
        删除购物车商品
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        #是不是最好还是要个序列化来做数据验证？
        account_id = request.data.get("account_id")
        course_ids = request.data.get("course_ids")
        conn = get_redis_connection()
        courses_dict_str = conn.hget('shopping_car', account_id)
        courses_dict = json.loads(courses_dict_str)
        for course_id in course_ids:
            del courses_dict[course_id]
        conn.hget("shopping_car", account_id, json.dumps(courses_dict))
        #这种删除怎么定义返回
        return Response(courses_dict)

    def put(self, request, *args, **kwargs):
        ss = serializer.ShoppingCarUpdateSerializers(instance=request.data, many=False)
        if ss.is_valid():
            conn = get_redis_connection()
            courses_dict_str = conn.hget("shopping_car", ss.account_id)
            courses_dict = json.loads(courses_dict_str)
            courses_dict[ss.course_id]['default_policy'] = ss.policy_id
            conn.hset('shopping_car', ss.account_id, json.dumps(courses_dict))
            return Response(ss.data)
        else:
            return Response(ss.errors)


