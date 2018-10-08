# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from ..repository.login import *

def login(*args, **kwargs):
    if kwargs.get("email"):
        if not find_one_by_email_and_password(kwargs.get("email"), kwargs.get("password")):
           return False, {"status":"error", "message":"邮箱不正确或密码不正确"}
    elif kwargs.get("username"):
        if not find_one_by_username_and_password(kwargs.get("username"), kwargs.get("password")):
            return False, {"status":"error", "message":"用户名不正确或密码不正确"}
    else:
        return False, {"status":"error", "message":"请输入邮箱或用户名"}

    return True,{}