from django.shortcuts import render,HttpResponse
from app01.models import *
from app01.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.db import models
class User(models.Model):

    username = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.username

def add(request):
    for i in range(100):
        User.objects.create(username='alex%s'%i, email='%s@qq.com'%i)
    return HttpResponse('ok')

def show(request):
    data_list = User.objects.all()
    full_path = request.get_full_path()
    print('full_path', full_path)
    paginator = Paginator(data_list, 8, full_path, 7) #每页8条  显示7个页码
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{'data':data})


