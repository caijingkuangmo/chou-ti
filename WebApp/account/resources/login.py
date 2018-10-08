# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


from flask import request
from flask_restful import Resource
from account import api
from ..services.login import *

class Login(Resource):
    '''
    {
        "email":"1174653067@qq.com",
        "username":"",
        "password":"123456"
    }
    '''
    def post(self):
        params = request.json
        if params.get("email", None) is None or params.get("username", None) is None or params.get("password", None) is None:
            return {"status":"error", "message":"参数有误"}

        status, info = login(**params)
        if not status:
            return info
        return {"status":"ok", "message":"登录成功"}


api.add_resource(Login, '/login')