# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from django_redis import get_redis_connection
import json

class RedisDictConnection:

    def __init__(self, key, field):
        self.conn = get_redis_connection()
        self.key = key
        self.field = field

    @property
    def value(self):
        val_str = self.conn.hget(self.key, self.field)
        try:
            val_dict = json.loads(val_str)
            return val_dict if val_dict else {}
        except:
            return val_str

    def set_val(self, val):
        if isinstance(val, str) or isinstance(val, bytes):
            val_str = val
        else:
            val_str = json.dumps(val)
        self.conn.hset(self.key, self.field, val_str)
