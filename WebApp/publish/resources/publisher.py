# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from flask import request
from flask_restful import Resource
from publish import api

from ..services.publish import *

class UrlTitle(Resource):

    def post(self):
        params = request.json
        if not params.get('url', None):
            return {"status":"error", "message":"参数有误"}

        return {"status":"ok","message":{"url":get_title(params.get('url'))}}

api.add_resource(UrlTitle, '/url-title')