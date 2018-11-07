# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from Xadmin.service.xadmin import site, ModelXadmin
from crm import models

from django.conf.urls import url
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse, redirect, render
from django.http import JsonResponse
from django.db.models import Q

import datetime

class UserConfig(ModelXadmin):
    list_display = ['id', 'name', 'email', 'depart']

site.register(models.UserInfo, UserConfig)


class ClassConfig(ModelXadmin):
    list_display = ['tutor', 'teachers']

site.register(models.ClassList, ClassConfig)


class ConsultConfig(ModelXadmin):
    list_display = ['customer', 'consultant', 'date', 'note']

site.register(models.ConsultRecord, ConsultConfig)


class CourseRecordConfig(ModelXadmin):
    def view_studyrecord(self, obj=None, header=False):
        if header:
            return "学习记录"
        return mark_safe("<a href='/xadmin/crm/studyrecord/?course_record=%s'>查看学习记录</a>"%obj.pk)

    def record_score(self, obj=None, header=False):
        if header:
            return "录入成绩"
        return mark_safe("<a href='record_score/%s'>录入成绩</a>"%obj.pk)

    list_display = ['class_obj', 'day_num', 'teacher', view_studyrecord, record_score]

    def record_score_view(self, request, course_record_id):
        '''
        从课程记录页面进入到 某个课程记录下面的所有学生学习记录 成绩编辑页面
        :param request:
        :param course_record_id:
        :return:
        '''
        if request.method == "POST":
            data = {}
            for key, value in request.POST.items():
                if key == "csrfmiddlewaretoken": continue
                field, pk = key.rsplit("_", 1)
                if pk in data:
                    data[pk][field] = value
                else:
                    data[pk] = {field:value}

            for pk, update_data in data.items():
                models.StudyRecord.objects.filter(pk=pk).update(**update_data)

            return redirect(request.path)

        else:
            study_record_list = models.StudyRecord.objects.filter(course_record=course_record_id)
            score_choices = models.StudyRecord.score_choices
            return render(request, "Xadmin/score.html", locals())


    def extra_url(self):
        temp = []
        temp.append(url(r"record_score/(\d+)", self.record_score_view))
        return temp

    def patch_studyrecord(self, request, queryset):
        #找到当前课程下的所有学生进行创建记录
        temp = []
        for course_record in queryset:
            student_list = models.Student.objects.filter(class_list__id=course_record.class_obj.pk)
            for student in student_list:
                obj = models.StudyRecord(student=student, course_record=course_record)
                temp.append(obj)
        models.StudyRecord.objects.bulk_create(temp)

    patch_studyrecord.short_description = '批量生成学习记录'
    actions = [patch_studyrecord,]

site.register(models.CourseRecord, CourseRecordConfig)


class CustomerConfig(ModelXadmin):
    def display_course(self, obj=None, header=False):
        if header:
            return "咨询课程"
        temp = []
        for course in obj.course.all():
            #取消谁的 哪个课程
            s = "<a href='/xadmin/crm/customer/cancel_course/%s/%s'" \
                "style='border:1px solid #369;padding:2px 5px;'>%s</a>" %(obj.pk, course.pk, course.name)
            temp.append(s)
        return mark_safe(" ".join(temp))

    list_display = ['name', 'gender', display_course, 'consultant', ]

    def cancel_course_view(self, request, customer_id, course_id):
        customer_obj = models.Customer.objects.filter(pk=customer_id).first()
        customer_obj.course.remove(course_id)
        return redirect(self.get_list_url())

    def public_customer(self, request):
        '''
        公共客户条件：未报名，且3天未跟进或者15天未成单
        日期差可用：  datetime.timedelta(days=3)
        :param request:
        :return:
        '''
        now = datetime.datetime.now()
        delta_day3 = datetime.timedelta(days=3)
        delta_day15 = datetime.timedelta(days=15)
        user_id = 5
        customer_list = models.Customer.objects.filter(
            Q(last_consult_date__lt=now-delta_day3)|Q(recv_date__lt=now-delta_day15), status=2
        ).exclude(consultant=user_id) #共有客户里 排除 是从自己手中变成公有客户
        return render(request, "Xadmin/public.html", locals())

    def further_customer(self, request, customer_id):
        '''
        跟进某个客户， 更改跟单时间，接单时间，跟进人，记录一条客户分布信息
        :param request:
        :param customer_id:
        :return:
        '''
        user_id = 7
        now = datetime.datetime.now()
        delta_day3 = datetime.timedelta(days=3)
        delta_day15 = datetime.timedelta(days=15)

        ret = models.Customer.objects.filter(pk=customer_id).filter(
            Q(last_consult_date__lt=now-delta_day3)|Q(recv_date__lt=now-delta_day15), status=2
        ).update(consultant=user_id, last_consult_date=now, recv_date=now)
        if not ret:
            return HttpResponse("已经被跟进了")

        models.CustomerDistrbute.objects.create(customer_id=customer_id, consultant_id=user_id, date=now, status=1)
        return HttpResponse("跟进成功")

    def mycustomer(self, request):
        user_id = 2
        customer_distrbute_list = models.CustomerDistrbute.objects.filter(consultant=user_id)
        return render(request, "Xadmin/mycustomer.html", locals())

    def extra_url(self):
        temp = []
        temp.append(url(r'cancel_course/(\d+)/(\d+)', self.cancel_course_view))
        temp.append(url(r'public/', self.public_customer))
        temp.append(url(r'further/(\d+)', self.further_customer))
        temp.append(url(r'mycustomer/', self.mycustomer))
        return temp

site.register(models.Customer, CustomerConfig)



class StudentConfig(ModelXadmin):

    def score_show(self, obj=None, header=False):
        if header:
            return "查看成绩"
        return mark_safe("<a href='/xadmin/crm/student/score_view/%s'>查看成绩</a>"%obj.pk)

    list_display = ['customer', 'class_list', score_show]
    list_display_links = ['customer']

    def extra_url(self):
        temp = []
        temp.append(url(r"score_view/(\d+)", self.score_show_view))
        return temp

    def score_show_view(self, request, student_id):
        '''
        显示所报班级，每个班级都可以点击查看 柱状图形式的课程成绩
        :return:
        '''
        if request.is_ajax():
            # 获取某个同学下  某个课程所有天的成绩, 成绩记录在学习记录表中
            student_id = request.GET.get("sid")
            class_id = request.GET.get("cid")
            study_record_list = models.StudyRecord.objects.filter(student=student_id, course_record__class_obj=class_id)
            data_list = []
            for study_record in study_record_list:
                day_num = study_record.course_record.day_num
                data_list.append(["day%s"%day_num, study_record.score])

            return JsonResponse(data_list, safe=False)
        else:
            student = models.Student.objects.filter(pk=student_id).first()
            class_list = student.class_list.all()
            return render(request, "Xadmin/score_view.html", locals())

site.register(models.Student, StudentConfig)


class StudyRecordConfig(ModelXadmin):
    list_display = ['student', 'course_record', 'record', 'score']

    def patch_late(self, request, queryset):
        queryset.update(record="late")

    patch_late.short_description = "迟到"
    actions = [patch_late,]

site.register(models.StudyRecord, StudyRecordConfig)


site.register(models.School)
site.register(models.Course)
site.register(models.Department)
site.register(models.CustomerDistrbute)