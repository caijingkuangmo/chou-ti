# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from infrastructure.account import *
from ..repository.register import *
from __init__ import db

def send_valid_code(email):
    code = send_code(email)
    if code:
        return insert_one_code(code, email)
    else:
        return False

def regist_user(params):
    if find_one_by_email_and_code(params.get('email'), params.get('code')):
        del params['code']
        delete_register_code(params.get('email'))
        insert_one_user_info(**params)
        db.session.commit()
        db.session.close()
        return True
    else:
        return False

def valid_email(email):
    '''
    验证邮箱格式？
    和验证是否注册过
    :param email:
    :return:
    '''
    if judge_send(email):
        return False, {"status":"error", "message":"验证码已经发送过"}

    if judge_register(email):
        return False, {"status":"error", "message":"邮箱已经注册过"}
    return True, {}


