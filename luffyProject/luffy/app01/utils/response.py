# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

class BaseResponse(object):

    def __init__(self):
        self.data = None
        self.code = 1000
        self.error = None

    @property
    def dict(self):
        return self.__dict__