# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'


class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = ""

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/testdb?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = -1
    DEBUG = True