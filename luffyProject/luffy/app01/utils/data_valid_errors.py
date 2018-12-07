# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

class PricePolicyInvalid(Exception):
    def __init__(self, msg):
        self.msg = msg


class CourseInvalid(Exception):

    def __init__(self, msg):
        self.msg = msg

class CouponInvalid(Exception):
    def __init__(self, msg):
        self.msg = msg

class BalanceInvalid(Exception):
    def __init__(self, msg):
        self.msg = msg

class PayMoneyInvalid(Exception):
    def __init__(self, msg):
        self.msg = msg