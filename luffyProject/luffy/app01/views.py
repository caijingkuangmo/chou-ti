from django.shortcuts import render, HttpResponse

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response

from app01 import models
from app01 import serializer
from app01.utils.account import get_random_str2

# class CourseView(APIView):
#     def get(self, request, *args, **kwargs):
#         courses = models.Course.objects.all()
#         cs = serializer.CourseSerializers(courses, many=True)
#         return Response(cs.data)


class CourseView(ViewSetMixin, APIView):
    authentication_classes = []
    def list(self, request, *args, **kwargs):
        '''
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {'code':1000, 'data':None}
        try:
            queryset = models.Course.objects.all()
            ser = serializer.CourseSerializers(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = "获取课程失败"
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        '''
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {'code':1000, 'data':None}
        try:
            #课程ID
            pk = kwargs.get('pk')
            obj = models.CourseDetail.objects.filter(course_id=pk).first()
            ser = serializer.CourseDetailSerializers(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = "获取课程详细失败"
        return Response(ret)

class CourseDetailView(APIView):

    def get(self, request, *args, **kwargs):
        couse_details = models.CourseDetail.objects.all()
        cds = serializer.CourseDetailSerializers(couse_details, many=True)
        return Response(cds.data)


class ChapterView(APIView):
    def get(self, request, *args, **kwargs):
        chapters = models.Chapter.objects.all()
        chas = serializer.ChapterSerializers(chapters, many=True)
        return Response(chas.data)


class LoginView(APIView):
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        pwd = request.data.get('pwd')
        user = models.UserInfo.objects.filter(user=name, pwd=pwd).first()
        res = {"state_code":1000, "msg":None}
        if user:
            random_str = get_random_str2()
            token = models.UserToken.objects.update_or_create(user=user, defaults={'token':random_str})
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