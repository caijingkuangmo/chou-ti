# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from infrastructure.publish import *
from ..repository.publish import *

def get_title(url):
    return get_url_title(url)

def valid_params(params, file=None):
    publish_type = params.get('publish_type', None)
    if publish_type == "link":
        if not params.get("url", None) or not params.get("title", None) or not params.get("user_info_id", None)\
            or not params.get("news_type_id") or params.get('content', None) is None:
                return False, {"status":"error", "message":"参数有误"}

    elif publish_type == "word":
        if not params.get("content", None) or not params.get("news_type_id", None) or not params.get("user_info_id", None):
            return False, {"status":"error", "message":"参数有误"}

    elif publish_type == "image":  #文件类型需要注意的
        if not params.get("content", None) or not params.get("news_type_id") or not params.get("user_info_id", None) or \
                (file is not None and not file):
            return False, {"status":"error", "message":"参数有误"}

    else:
        return False, {"status":"error", "message":"发布类型有误"}

    return True, {}


def publish_news(params, file):

    publish_type = params.get('publish_type', None)
    del params['publish_type']
    if publish_type == "link":
        publish_link_info(**params)
    elif publish_type == "word":
        publish_word_info(**params)
    elif publish_type == "image":
        publish_image_info(file, **params)

