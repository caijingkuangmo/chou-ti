# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from Xadmin.service.xadmin import site, ModelXadmin
from app01 import models


site.register(models.UserInfo)

class CourseConfig(ModelXadmin):
    list_display = ['title', 'level']
site.register(models.Course, CourseConfig)


class CourseDetailConfig(ModelXadmin):
    list_display = ['course', 'slogon', 'why', 'recommend_courses']

site.register(models.CourseDetail, CourseDetailConfig)


class ChapterConfig(ModelXadmin):
    list_display = ['num', 'name', 'course']

site.register(models.Chapter, ChapterConfig)


class UserTokenConfig(ModelXadmin):
    list_display = ['user', 'token']

site.register(models.UserToken, UserTokenConfig)