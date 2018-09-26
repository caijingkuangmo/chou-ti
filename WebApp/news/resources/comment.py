# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from flask import request
from flask_restful import Resource
from news import api

class Comment(Resource):

    def get(self):
        return {"message":"comment"}

    def post(self):
        return {"":""}

api.add_resource(Comment, '/comment/get')
