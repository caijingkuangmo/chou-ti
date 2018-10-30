# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'


class BasePermission(object):
    message = None
    def has_permission(self, view):
        raise NotImplemented('必须重写has_permission方法')

class AllowAny(BasePermission):
    def has_permission(self, view):
        return True