# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from Xadmin.service.xadmin import site, ModelXadmin
from app01 import models


site.register(models.CourseCategory)
site.register(models.CourseSubCategory)

class AccountConfig(ModelXadmin):
    list_display = ['id', 'username']
site.register(models.Account, AccountConfig)

class CourseConfig(ModelXadmin):
    list_display = ['id', 'name', 'sub_category', 'course_type', 'degree_course', 'level']
site.register(models.Course, CourseConfig)

class DegreeCourseConfig(ModelXadmin):
    list_display = ['name', 'brief', 'total_scholarship', 'mentor_compensation_bonus', 'prerequisite', 'teachers']
site.register(models.DegreeCourse, DegreeCourseConfig)

class TeacherConfig(ModelXadmin):
    list_display = ['name', 'role', 'title', 'brief']
site.register(models.Teacher, TeacherConfig)

class CourseDetailConfig(ModelXadmin):
    list_display = ['course', 'hours', 'course_slogan', 'why_study', 'recommend_courses', 'teachers']
site.register(models.CourseDetail, CourseDetailConfig)


class CourseChapterConfig(ModelXadmin):
    list_display = ['chapter', 'name', 'course']
site.register(models.CourseChapter, CourseChapterConfig)


class UserAuthTokenConfig(ModelXadmin):
    list_display = ['user', 'token']
site.register(models.UserAuthToken, UserAuthTokenConfig)


site.register(models.ArticleSource)

class ArticleConfig(ModelXadmin):
    list_display = ['title', 'source', 'article_type', 'brief', 'vid', 'comment_num', 'agree_num', 'view_num', 'collect_num']
site.register(models.Article, ArticleConfig)


class CollectionConfig(ModelXadmin):
    list_display = ['content_type', 'object_id', 'account']
site.register(models.Collection, CollectionConfig)

class CommentConfig(ModelXadmin):
    list_display = ['content_type', 'object_id', 'p_node', 'content', 'account', 'disagree_number', 'agree_number']
site.register(models.Comment, CommentConfig)


class PricePolicyConfig(ModelXadmin):
    list_display = ['id', 'content_type', 'object_id', 'valid_period', 'price']
site.register(models.PricePolicy, PricePolicyConfig)


class CourseSectionConfig(ModelXadmin):
    list_display = ['chapter', 'name', 'section_type']
site.register(models.CourseSection, CourseSectionConfig)


class CouponConfig(ModelXadmin):
    list_display = ['name', 'coupon_type', 'money_equivalent_value', 'off_percent', 'minimum_consume', 'content_type', 'object_id', 'valid_begin_date', 'valid_end_date']
site.register(models.Coupon, CouponConfig)

class CouponRecordConfig(ModelXadmin):
    list_display = ['coupon', 'number', 'account', 'status']
site.register(models.CouponRecord, CouponRecordConfig)