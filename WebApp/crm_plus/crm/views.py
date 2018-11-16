from django.shortcuts import render, HttpResponse

from crm import models
from rbac.models import Permission, PermissionGroup
# Create your views here.

curd = [
    {
        'title' : "查看",
        "url" : "/",
        "action" : "list",
    },
    {
        'title': "编辑",
        "url": "/(\d+)/change/",
        "action": "edit",
    },
    {
        'title': "删除",
        "url": "/(\d+)/delete/",
        "action": "delete",
    },
    {
        'title': "添加",
        "url": "/add/",
        "action": "add",
    },
]

table_map = {
    'classlist':{
        'group_name': "班级管理",
        'title':"班级",
        'model': models.ClassList,
    },
    'consultrecord': {
        'group_name': "客户跟进记录管理",
        'title': "客户跟进记录",
        'model': models.ConsultRecord,
    },
    'courserecord': {
        'group_name': "上课记录管理",
        'title': "上课记录",
        'model': models.CourseRecord,
    },
    'customer': {
        'group_name': "客户管理",
        'title': "客户",
        'model': models.Customer,
    },
    'student': {
        'group_name': "学生管理",
        'title': "学生",
        'model': models.Student,
    },
    'studyrecord': {
        'group_name': "学习记录管理",
        'title': "学习记录",
        'model': models.StudyRecord,
    },
    'school': {
        'group_name': "校区管理",
        'title': "校区",
        'model': models.School,
    },
    'course': {
        'group_name': "课程管理",
        'title': "课程",
        'model': models.Course,
    },
}


def add_permissions(request):
    # permission_list = []
    for table_name, item in table_map.items():
        per_group = PermissionGroup.objects.filter(title=item["group_name"]).first()
        print(per_group)
        for operation in curd:
            permiss = Permission(
                title=operation['title'] + item['title'],
                url='/xadmin/crm/' + table_name + operation['url'],
                action=operation['action'],
                group=per_group
            )
            permiss.save()
            # permission_list.append(Permission)
    # Permission.objects.bulk_create(permission_list)
    return HttpResponse("ok")


from rbac.models import User
from rbac.service.permissions import initial_session
def login(request):
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get("pwd")
        user_obj = User.objects.filter(name=user, pwd=pwd).first()
        if user_obj:
            request.session["user_id"] = user_obj.pk
            initial_session(user_obj, request)
            return HttpResponse("登录成功")

    return render(request, 'login.html')