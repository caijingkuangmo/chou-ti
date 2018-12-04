# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from rest_framework.views import APIView

'''
结算时写入redis的数据结构：
    主要是两块：课程信息和优惠券信息
    1.课程信息：
        标题，图片，有效期，价格
    2.优惠券：
        课程优惠券 优惠券id，类型，编号，使用状态，课程ID
        全局优惠券 优惠券id，类型，编号，使用状态，课程ID 0
    
    {
        "pay_bill_用户ID_coupon_券ID"：{
            优惠券id：1，
            类型：通用券，
            编号：2，
            使用状态：未使用，
            满减多少，折扣多少...
            课程ID：2  #全局默认为0
        }，
        pay_bill_用户ID_course_课程ID:{
            标题，图片，策略ID, 有效期，价格，优惠券字典，默认优惠券ID(默认为0)
        }
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
    def post(self, request, *args, **kwargs):
        '''去结算，把结算商品和优惠券写入redis'''
        pass

    def patch(self, request, *args, **kwargs):
        '''修改优惠券，包括课程的和所有的'''
        pass

    def get(self, request, *args, **kwargs):
        '''查看计算商品'''
        pass