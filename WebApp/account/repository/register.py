# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import time

from db import models
from __init__ import db


def insert_one_code(code, email):
    if not db.session.add(models.SendCode(email=email, code=code, status=0, stime=time.time())):
        return False
    db.session.commit()
    db.session.close()
    return True

def find_one_by_email_and_code(email, code):
    obj = db.session.query(models.SendCode).filter_by(email=email, code=code).first()
    return True if obj else False

def insert_one_user_info(*args, **kwargs):
    return True if db.session.add(models.UserInfo(**kwargs)) else False