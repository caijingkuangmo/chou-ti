from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from rbac.models import User, Role
from rbac.service.permissions import initial_session

class PermissionOperation(object):
    def __init__(self, actions):
        self.actions = actions

    def add(self):
        return "add" in self.actions

    def delete(self):
        return "delete" in self.actions

    def edit(self):
        return "edit" in self.actions

    def list(self):
        return "list" in self.actions

def login(request):
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get("pwd")

        user_obj = User.objects.filter(name=user, pwd=pwd).first()
        if user_obj:
            request.session['user_id'] = user_obj.pk
            initial_session(user_obj, request)
            return HttpResponse("登录成功")

    return render(request, 'login.html')

def users(request):
    user_list = User.objects.all()

    user_id = request.session.get('user_id')
    user = User.objects.filter(id=user_id).first()

    per = PermissionOperation(request.actions)
    return render(request, "rbac/users.html", locals())

def add_user(request):

    return HttpResponse("add user")

def del_user(request, id):
    return HttpResponse('delete user')

def edit_user(request):
    return HttpResponse('edit user')

def roles(request):
    user_id = request.session.get("user_id")
    user = User.objects.filter(id=user_id).first()

    role_list = Role.objects.all()
    per = PermissionOperation(request.actions)
    return render(request, "rbac/roles.html", locals())
