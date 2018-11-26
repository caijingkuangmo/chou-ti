# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from rest_framework.views import APIView
from rest_framework.response import Response
from app01 import models
from app01.utils.account import get_random_str2


class LoginView(APIView):
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.Account.objects.filter(username=username, password=password).first()
        res = {"state_code":1000, "msg":None}
        if user:
            random_str = get_random_str2()
            token = models.UserAuthToken.objects.update_or_create(user=user, defaults={'token':random_str})
            res["token"] = random_str
        else:
            res["state_code"] = 1001
            res["msg"] = "用户名或密码错误"

        import json
        # return Response(json.dumps(res, ensure_ascii=False))
        return Response(res)


class LogoutView(APIView):
    authentication_classes = []
    def post(self, *args, **kwargs):
        return Response("ok")