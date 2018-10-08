# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import time
from datetime import datetime

from db import models
from __init__ import db


def insert_one_code(code, email):
    db.session.add(models.SendCode(email=email, code=code, status=0, stime=datetime.utcnow()))
    db.session.commit()
    db.session.close()
    return True

def find_one_by_email_and_code(email, code):
    obj = db.session.query(models.SendCode).filter_by(email=email, code=code).first()
    return True if obj else False

def insert_one_user_info(*args, **kwargs):
    '''
    插入一条用户信息
    :param args:
    :param kwargs:
    :return:
    '''
    kwargs['ctime'] = datetime.utcnow()
    return True if db.session.add(models.UserInfo(**kwargs)) else False

def delete_register_code(email):
    '''
    删除临时验证码信息
    :param email:
    :return:
    '''
    return True if db.session.query(models.SendCode).filter_by(email=email).delete() else False

def judge_send(email):
    '''
    判断是否发送过信息
    :param email:
    :return: 发送过 True   没发送False
    '''
    return True if db.session.query(models.SendCode).filter_by(email=email).first() else False

def judge_register(email):
    '''
    判断是否注册过
    :param email:
    :return: 注册过True  没注册False
   '''
    return True if db.session.query(models.UserInfo).filter_by(email=email).first() else False