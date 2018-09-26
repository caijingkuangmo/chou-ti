# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import request
from flask_restful import Resource
from account import api

from ..services.register import *

'''
接收哪些信息：
    邮箱，验证码，密码
    邮箱是否注册过？  验证码是否对上？ 是否满足密码负责度？
    临时存储邮箱和验证码，时效性考虑
'''

class Register(Resource):

    def post(self):
        params = request.json
        if not params.get('email', None) or not params.get('username', None) \
            or not params.get('password', None) or not params.get('code', None):
                return {'status':'error', 'message':'Incomplete data'}

        if not regist_user(params):
            return {'status':'error', 'message':'验证码错误！'}
        return {'status':'ok', 'message':'注册成功'}

class ValidCode(Resource):

    def post(self):
        params = request.json
        email = params.get('email', None)
        if email:
            send_valid_code(email)
            return {'status':'ok', 'message':'验证码发送成功'}
        else:
            return {'status':'error', 'message':'请输入邮箱或邮箱格式不对'}

api.add_resource(Register, '/register')
api.add_resource(ValidCode, '/send-valid-code')