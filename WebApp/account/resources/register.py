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
    邮箱是否注册过？  验证码是否对上？     是否满足密码负责度？（放后）
    临时存储邮箱和验证码，    时效性考虑（放后）   
'''


class Register(Resource):
    '''
    {
        "email": "1174653067@qq.com",
        "username": "seven",
        "password": "123456",
        "code": "4C2V"
    }
    '''
    def post(self):
        params = request.json
        if not params.get('email', None) or not params.get('username', None) \
            or not params.get('password', None) or not params.get('code', None):
                return {'status':'error', 'message':'Incomplete data'}

        if not regist_user(params):
            return {'status':'error', 'message':'验证码错误！'}
        return {'status':'ok', 'message':'注册成功'}

'''
验证流程：
    第一步：获取验证码   携带邮箱，判断邮箱是否在临时表中，有就不发送邮件（提示已发送）
                                                没有就发送，并记录到临时表中（还要判断是否注册过）
    
    第二步：注册，携带所有的信息，邮箱，验证码，用户名，密码    对用户名的唯一性进行判断（放后）
                判断邮箱和验证码是否正确，正确就返回在用户表插入信息，删除临时表记录
'''

class ValidCode(Resource):
    '''
    {
	    "email":"1174653067@qq.com"
    }
    '''
    def post(self):
        params = request.json
        email = params.get('email', None)
        if email:
            status, message = valid_email(email)
            if not status:
                return message
            if send_valid_code(email):
                return {"status":"ok", "message":"验证码发送成功"}
            else:
                return {"status":"error", "message":"发送失败，请检测邮箱是否填写正确"}
        else:
            return {"status":"error", "message":"请输入邮箱"}

api.add_resource(Register, '/register')
api.add_resource(ValidCode, '/send-valid-code')