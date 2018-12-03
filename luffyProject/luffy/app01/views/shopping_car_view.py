# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'


from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
import json
import copy

from app01 import serializer
from app01 import models
from app01.utils.redis_pool import RedisDictConnection

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

class ShoppingCarView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        '''
        查看购物车
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        account_id = request.GET.get('account_id')
        redis_conn = RedisDictConnection('shopping_car',account_id)
        course_dict = redis_conn.value
        return Response({'code':1000, 'data':course_dict if course_dict else {}})

    def post(self, request, *args, **kwargs):
        '''
        添加到购物车
        {
            "account_id":1,
            "course_id":5,
            "policy_id":5
        }
        :param args:
        :param kwargs:
        :return:
        '''
        ss = serializer.ShoppingCarAddSerializers(data=request.data, many=False)
        if ss.is_valid():
            #验证价格合法性
            course_obj = models.Course.objects.filter(id=ss.data.get('course_id')).first()
            price_policy_list = course_obj.price_policy.all()
            filter_result = filter(lambda item: item.id == ss.data.get("policy_id"), price_policy_list)
            if list(filter_result):
                #写入redis
                ass = serializer.ShoppingCarShowSerializers(instance=course_obj, many=False)
                add_data = copy.deepcopy(ass.data)
                add_data['default_policy'] = ss.data.get('policy_id')
                redis_conn = RedisDictConnection('shopping_car', ss.data.get("account_id"))
                #先把用户之前的购物车数据取出来
                buy_car = redis_conn.value
                buy_car[ss.data.get('course_id')] = add_data
                redis_conn.set_val(buy_car)
                return Response(ss.data)
            else:
                return Response({'code':1001, 'message':'price policy id is error', 'data':{}})
        else:
            return Response(ss.errors)

    def delete(self, request, *args, **kwargs):
        '''
        删除购物车商品
        {
            "account_id":1,
            "course_ids":[5,6]
        }
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        #是不是最好还是要个序列化来做数据验证？
        account_id = request.data.get("account_id")
        course_ids = request.data.get("course_ids")
        redis_conn = RedisDictConnection('shopping_car', account_id)
        courses_dict = redis_conn.value
        for course_id in course_ids:
            del courses_dict[str(course_id)]  #插入和读取时的数据类型 注意一下
        redis_conn.set_val(courses_dict)
        #这种删除怎么定义返回
        return Response({'code':1000, 'data':courses_dict})

    def put(self, request, *args, **kwargs):
        '''
        修改价格策略
        {
            "account_id": 1,
            "course_id": 5,
            "policy_id": 4
        }
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ss = serializer.ShoppingCarUpdateSerializers(data=request.data, many=False)
        if ss.is_valid():
            redis_conn = RedisDictConnection("shopping_car", ss.data.get("account_id"))
            courses_dict = redis_conn.value
            courses_dict[str(ss.data.get("course_id"))]['default_policy'] = ss.data.get("policy_id")
            redis_conn.set_val(courses_dict)
            return Response(ss.data)
        else:
            return Response(ss.errors)


