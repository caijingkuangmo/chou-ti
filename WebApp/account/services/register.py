# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from infrastructure.account import *
from ..repository.register import *

def send_valid_code(email):
    code = send_code(email)
    if code:
        return insert_one_code(code, email)
    else:
        return False

def regist_user(params):
    if find_one_by_email_and_code(params.get('email'), params.get('code')):
        return insert_one_user_info(**params)
    else:
        return False