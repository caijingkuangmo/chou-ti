# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


from flask import request
from flask_restful import Resource
from account import api

class Receive(Resource):


    def get(self):
        return {'message':'456'}

    def post(self):
        print(request.files)
        request.files['file'].save('static/img/' + request.files['file'].filename)
        return {'message':'123'}


api.add_resource(Receive, '/upload')
