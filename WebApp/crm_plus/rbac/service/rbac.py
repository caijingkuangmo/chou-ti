# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import re
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

#设置不进行权限验证的白名单
white_list = ["/login/", "/reg/", "/admin/.*"]

def valid_white_url(current_path):
    for valid_url in white_list:
        ret = re.match(valid_url, current_path)
        if ret:
            return True
    return False

def auth_login(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("/login/")
    else:
        return None

class ValidPermission(MiddlewareMixin):
    def process_request(self, request):
        current_path = request.path_info

        #白名单验证
        if valid_white_url(current_path):
            return None

        #登录验证
        auth_result = auth_login(request)
        if auth_result is not None:
            return auth_result

        #权限校验
        permission_dict = request.session.get("permission_dict")
        for permission_item in permission_dict.values():
            urls = permission_item['urls']
            for url_reg in urls:
                url_reg = "^%s$"%url_reg
                ret = re.match(url_reg, current_path)
                if ret:
                    request.actions = permission_item['actions'] #用于前端操作按钮控制
                    return None

        return HttpResponse("没有访问权限")
