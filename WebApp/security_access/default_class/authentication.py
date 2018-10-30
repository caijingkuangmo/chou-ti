# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import request

class BaseAuthentication(object):

    def authenticate(self, view=None):
        raise NotImplemented("必须重写authenticate方法")

class UsernameAuthentication(BaseAuthentication):

    def authenticate(self, view=None):
        print('auth')
        user = getattr(request.json, 'user', None) or getattr(request.json, 'username', None)
        if not user:
            return None
        return (user, None)
