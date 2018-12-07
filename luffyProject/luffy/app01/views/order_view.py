# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django_redis import get_redis_connection
from django.db import transaction

from app01.utils.response import BaseResponse
from app01.utils.data_valid_errors import BalanceInvalid, PayMoneyInvalid
from app01 import models
from app01.utils.account import get_random_str2

class OrderView(APIView):
    redis_conn = get_redis_connection()
    def post(self, request, *args, **kwargs):
        """
        立即支付
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        """
        1. 获取用户提交数据
                {
                    balance:1000,
                    money:900
                }
           balance = request.data.get("balance")
           money = request.data.get("money")

        2. 数据验证
            - 大于等于0
            - 个人账户是否有1000贝里

            if user.auth.user.balance < balance:
                账户贝里余额不足

        优惠券ID_LIST = [1,3,4]
        总价
        实际支付
        3. 去结算中获取课程信息
            for course_dict in redis的结算中获取：
                # 获取课程ID
                # 根据course_id去数据库检查状态

                # 获取价格策略
                # 根据policy_id去数据库检查是否还依然存在

                # 获取使用优惠券ID
                # 根据优惠券ID检查优惠券是否过期

                # 获取原价+获取优惠券类型
                    - 立减
                        0 = 获取原价 - 优惠券金额
                        或
                        折后价格 = 获取原价 - 优惠券金额
                    - 满减：是否满足限制
                        折后价格 = 获取原价 - 优惠券金额
                    - 折扣：
                        折后价格 = 获取原价 * 80 / 100

        4. 全站优惠券
            - 去数据库校验全站优惠券的合法性
            - 应用优惠券：
                - 立减
                    0 = 实际支付 - 优惠券金额
                    或
                    折后价格 =实际支付 - 优惠券金额
                - 满减：是否满足限制
                    折后价格 = 实际支付 - 优惠券金额
                - 折扣：
                    折后价格 = 实际支付 * 80 / 100
            - 实际支付
        5. 贝里抵扣

        6. 总金额校验
            实际支付 - 贝里 = money:900

        7. 为当前课程生成订单

                - 订单表创建一条数据 Order
                    - 订单详细表创建一条数据 OrderDetail   EnrolledCourse
                    - 订单详细表创建一条数据 OrderDetail   EnrolledCourse
                    - 订单详细表创建一条数据 OrderDetail   EnrolledCourse

                - 如果有贝里支付
                    - 贝里金额扣除  Account
                    - 交易记录     TransactionRecord

                - 优惠券状态更新   CouponRecord

                注意：
                    如果支付宝支付金额0，  表示订单状态：已支付
                    如果支付宝支付金额110，表示订单状态：未支付
                        - 生成URL（含订单号）
                        - 回调函数：更新订单状态
        """
        ret = BaseResponse()

        # 获取用户数据
        user_id = request.auth.user_id
        user = request.auth.user
        balance = request.data.get('balance')  #扣减贝里数
        money = request.data.get('money') #需要支付金额

        #判断贝里金额的合理性
        if balance > user.balance:
            raise BalanceInvalid("贝里金额不合法")

        #判断支付金额合理性
        if money < 0:
            raise PayMoneyInvalid("支付金额不合法")

        #从结算中获取 课程信息， 优惠券信息， 总金额， 实际支付金额
        course_match = settings.PAYMENT_COURSE_KEY %(user_id, '*', )
        coupon_match = settings.PAYMENT_COUPON_KEY %(user_id, '*', )
        global_coupon_key = settings.PAYMENT_GLOBAL_COUPON_KEY %(user_id, )

        total_pay_money = 0  #实际支付金额
        total_money = 0  #原价
        pay_coupon_list = []
        pay_course_list = []

        for course_key in self.redis_conn.scan_iter(course_match):
            #验证课程是否还存在
            course_id = self.redis_conn.hget(course_key, 'id').decode('utf-8')
            course_obj = models.Course.objects.filter(id=course_id).first()
            if not course_obj:
                ret.code = 2001
                ret.error = "课程不存在"
                return Response(ret.dict)

            #验证价格策略是否还存在
            policy_id = self.redis_conn.hget(course_key, 'policy_id').decode('utf-8')
            policy_obj = models.PricePolicy.objects.filter(id=policy_id).first()
            if not policy_obj:
                ret.code = 3001
                ret.error = "价格策略不合法"
                return Response(ret.dict)
            total_pay_money += policy_obj.price
            total_money += policy_obj.price

            #验证课程优惠券是否有效
            coupon_id = self.redis_conn.hget(course_key, 'coupon_id').decode('utf-8')
            if coupon_id != '0': #使用课程优惠券
                coupon_obj = models.CouponRecord.objects.filter(id=coupon_id).first()
                if not coupon_obj:
                    ret.code = 4002
                    ret.error = "课程优惠券不合法"
                    return Response(ret.dict)

                now_date = datetime.date.today()
                if coupon_obj.status != 0 or coupon_obj.valid_begin_date > now_date or coupon_obj.valid_end_date < now_date:
                    ret.code = 4003
                    ret.error = "课程优惠券无效"
                    return Response(ret.dict)
                pay_coupon_list.append(coupon_id)

                #计算课程 优惠券减少金额
                discount_money = 0
                if coupon_obj.coupon.coupon_type == 0:  # 通用券
                    discount_money = coupon_obj.coupon.money_equivalent_value
                elif coupon_obj.coupon.coupon_type == 1:  # 满减券
                    if policy_obj.price >= coupon_obj.coupon.minimum_consume:
                        discount_money = coupon_obj.coupon.money_equivalent_value
                elif coupon_obj.coupon.coupon_type == 2:  # 折扣券
                    discount_money = policy_obj.price * (100 - coupon_obj.coupon.off_percent) / 100
                total_pay_money -= discount_money
                pay_course_list.append({
                    'course': course_obj,
                    'policy': policy_obj,
                    'discount_money': discount_money, #优惠多少
                })



        #验证全局优惠券合理性
        global_coupon_id = self.redis_conn.get(global_coupon_key).decode('utf-8')
        if global_coupon_id != '0': #使用全局优惠券
            global_coupon_obj = models.CouponRecord.objects.filter(id=global_coupon_id).first()
            if not global_coupon_obj:
                ret.code = 4005
                ret.error = "全局优惠券不合法"
                return Response(ret.dict)

            now_date = datetime.date.today()
            if global_coupon_obj.status != 0 or global_coupon_obj.valid_begin_date > now_date or global_coupon_obj.valid_end_date < now_date:
                ret.code = 4006
                ret.error = "全局优惠券无效"
                return Response(ret.dict)
            pay_coupon_list.append(global_coupon_id)

            # 计算全局 优惠券减少金额
            if global_coupon_obj.coupon.coupon_type == 0:  # 通用券
                total_pay_money -= global_coupon_obj.coupon.money_equivalent_value
            elif global_coupon_obj.coupon.coupon_type == 1:  # 满减券
                if total_pay_money >= global_coupon_obj.coupon.minimum_consume:
                    total_pay_money -= global_coupon_obj.coupon.money_equivalent_value
            elif global_coupon_obj.coupon.coupon_type == 2:  # 折扣券
                total_pay_money -= total_pay_money * (100 - global_coupon_obj.coupon.off_percent) / 100

        # 抵扣个人账户贝里余额
        berri_balance = user.balance - balance
        total_pay_money -= balance

        # 前端支付金额和后端支付金额对比
        if money != total_pay_money:
            ret.code = 5001
            ret.error = "支付金额有出路"
            return Response(ret.dict)

        # 生成订单 和 支付记录
        with transaction.atomic():
            # 生成订单
            order_obj = models.Order.objects.create(**{
                'status': 1,
                'payment_type': 1,
                'order_number': get_random_str2(),
                'actual_amount': total_pay_money,
                'account': user,
            })

            # 生成课程报名记录  和 订单详细
            for course_dict in pay_course_list:
                course = course_dict['course']
                policy = course_dict['policy']
                dis_money = course_dict['discount_money']
                order_detail = models.OrderDetail.objects.create(**{
                    'content_object': models.OrderDetail.objects.get(id=course.id),
                    'order': order_obj,
                    'original_price': policy.price,
                    'price': policy.price - dis_money,
                    'valid_period_display': policy.get_valid_period_display(),
                    'valid_period': policy.valid_period,
                })

                models.EnrolledCourse.objects.create(**{
                    'account': user,
                    'course': course,
                    'order_detail': order_detail,
                    'valid_begin_date': datetime.date.today(),
                    'valid_end_date': datetime.date.today() + datetime.timedelta(days=policy.valid_period),
                })

            # 抵扣贝里， 生成贝里流水
            models.Account.objects.filter(id=user_id).update(balance=berri_balance)
            models.TransactionRecord.objects.create({
                'account': user,
                'amount': balance,
                'transaction_type': 1,
                'content_object': order_obj,
                'transaction_number': get_random_str2(),
            })

            #更新优惠券
            models.CouponRecord.filter(id__in=pay_coupon_list).update(status=1)

        # 如果支付宝支付金额0，  表示订单状态：已支付
        # 如果支付宝支付金额110，表示订单状态：未支付
        # - 生成URL（含订单号）
        # - 回调函数：更新订单状态
        return Response(ret.dict)