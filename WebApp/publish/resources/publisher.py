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

'''
加入对url的验证
'''

class UrlTitle(Resource):
    '''
    {
	    "url":"http://www.baidu.com"
    }
    '''
    def post(self):
        params = request.json
        if not params.get('url', None):
            return {"status":"error", "message":"参数有误"}

        try:
            title = get_title(params.get('url'))
        except:
            return {"status":"error", "message":"请检查url是否写全"}
        return {"status":"ok","message":{"url":title}}

'''

    nid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_info_id = db.Column(db.Integer, db.ForeignKey("userinfo.nid"))
    news_type_id = db.Column(db.Integer, db.ForeignKey("newstype.nid"))
    # ctime = db.Column(db.TIMESTAMP)
    ctime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    title = db.Column(db.String(32))
    url = db.Column(db.String(128))
    content = db.Column(db.String(150))

    链接：publish_type = link
        user_info_id, url, title, content(可空), news_type_id
    
    文字:publish_type = word
        user_info_id, content, news_type_id
    
    图片: publish_type = image
        user_info_id, files, content, news_type_id
    
'''

class PublishInfo(Resource):

    def post(self):
        status, info = valid_params(request.form, request.files)
        if not status:
            return info

        publish_news(request.form, request.files)
        print('form--', request.form)
        print('files--', request.files)
        # file = request.files['files']
        # print('----', file)
        # file.save('static/img/' + secure_filename(file.filename))
        pass


api.add_resource(UrlTitle, '/url-title')
api.add_resource(PublishInfo, '/publish-info')