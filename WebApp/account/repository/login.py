# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __init__ import db
from db import models

def find_one_by_email_and_password(email, password):
    return True if db.session.query(models.UserInfo).filter_by(email=email, password=password).first() else False

def find_one_by_username_and_password(username, password):
    return True if db.session.query(models.UserInfo).filter_by(username=username, password=password).first() else False