# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

class PricePolicyInvalid(Exception):
    def __init__(self, msg):
        self.msg = msg