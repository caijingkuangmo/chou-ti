# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.db.models import Q
from django.db.models.fields.related import ManyToManyField, ForeignKey
import copy
import json

from Xadmin.utils.paginator import Paginator, PageNotAnInteger, EmptyPage, NoDataPage

#定义默认配置模型类
class ModelXadmin:
    list_display = ['__str__',]
    list_display_links = []
    modelform_class = None
    search_fields = []
    actions = []
    list_filter = []

    def patch_delete(self, request, queryset):
        queryset.delete()
    patch_delete.short_description = "批量删除"

    def extra_url(self):
        return []

    def __init__(self, model, site):
        self.model = model
        self.site = site


    def get_change_url(self, obj):
        '''反向生成 修改url'''
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url = reverse("%s_%s_change"%(app_label, model_name), args=(obj.pk,))
        return _url

    def get_delete_url(self, obj):
        '''反向生成 删除url'''
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url = reverse("%s_%s_delete"%(app_label, model_name), args=(obj.pk,))
        return _url

    def get_add_url(self):
        '''反向生成 添加url'''
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url = reverse("%s_%s_add"%(app_label, model_name))
        return _url

    def get_list_url(self):
        '''反向生成 展示url'''
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url = reverse("%s_%s_list"%(app_label, model_name))
        return _url


    @property
    def curd_urls(self):
        return self.get_curd_urls(), None, None

    def get_curd_urls(self):
        '''构建 增删改查 4条url'''
        temp = []

        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label

        temp.append(url(r"^add/", self.add_view, name="%s_%s_add"%(app_label, model_name)))
        temp.append(url(r"^(\d+)/delete/", self.delete_view, name="%s_%s_delete"%(app_label, model_name)))
        temp.append(url(r"^(\d+)/change/", self.change_view, name="%s_%s_change"%(app_label, model_name)))
        temp.append(url(r"^$", self.list_view, name="%s_%s_list"%(app_label, model_name)))

        #扩展url
        temp.extend(self.extra_url())
        return temp


    def add_view(self, request):
        model_form_class = self.get_modelform_class()
        form = model_form_class()

        #pop功能实现
        for bfield in form:
            #打印bfield类型，就知道bfield是BoundField对象
            #bfield.field 获取字段
            #bfield.name 字段名称，用于构造url
            from django.forms.models import ModelChoiceField
            from django.forms.models import ModelMultipleChoiceField
            if isinstance(bfield.field, ModelChoiceField):
                bfield.is_pop = True
                #获取form field字段 对应模型表 bfield.field.queryset.model
                related_model_name = bfield.field.queryset.model._meta.model_name
                related_app_label = bfield.field.queryset.model._meta.app_label
                _url = reverse("%s_%s_add"%(related_app_label, related_model_name))
                #pop_res_id主要用于  在pop添加数据后，在添加页面确定哪个响应项
                bfield.url = _url + "?pop_res_id=id_%s"%bfield.name



        if request.method == "POST":
            form = model_form_class(request.POST)
            if form.is_valid():
                obj = form.save()

                #区分是pop添加还是 正常添加， pop添加 完成后跳转到 pop页面
                pop_res_id = request.GET.get("pop_res_id")
                if pop_res_id:
                    '''为什么这里要分开写？？？？不用locals()'''
                    #因为新添加的对象，要显示到页面上，所以需要返回新对象的id和内容
                    res = {"pk":obj.pk, "text":str(obj), "pop_res_id":pop_res_id}
                    return render(request, 'pop.html', {"res":res})

                return redirect(self.get_list_url())

        return render(request, 'add_view.html', locals())

    def delete_view(self, request, id):
        url = self.get_list_url()  #还要用于 前端渲染取消按钮  以回到展示页面
        if request.method == "POST":
            self.model.objects.filter(pk=id).delete()
            return redirect(url)
        return render(request, 'delete_view.html', locals())

    def change_view(self, request, id):
        model_form_class = self.get_modelform_class()
        edit_obj = self.model.objects.filter(pk=id).first()

        if request.method == "POST":
            form = model_form_class(request.POST, instance=edit_obj)
            if form.is_valid():
                form.save()
                return redirect(self.get_list_url())
            return render(request, "change_view.html", locals())
        form = model_form_class(instance=edit_obj)
        return render(request, 'change_view.html', locals())

    def list_view(self, request):
        if request.method == "POST": #action操作
            action = request.POST.get("action")
            selected_pk = request.POST.getlist("selected_pk")
            action_func = getattr(self, action)
            queryset = self.model.objects.filter(pk__in=selected_pk)
            action_func(request, queryset)

        #获取搜索 Q对象
        search_condition = self.get_search_conditon(request)

        #获取filter Q对象
        filter_condition = self.get_filter_condition(request)

        data_list = self.model.objects.all().filter(search_condition).filter(filter_condition)

        #构建表格数据
        showlist = ShowList(data_list, self, request)

        add_url = self.get_add_url() #主要用于前端添加按钮渲染
        return render(request, 'list_view.html', locals())


    '''为什么是pk？'''
    def edit(self, obj=None, header=False):
        '''编辑列'''
        if header:
            return "操作"
        # return mark_safe("<a href='%s/change'>编辑</a>"%obj.pk)
        return mark_safe("<a href='%s'>编辑</a>"%self.get_change_url(obj))

    def deletes(self, obj=None, header=False):
        '''删除列'''
        if header:
            return "操作"
        # return mark_safe("<a href='%s/delete'>删除</a>"%obj.pk)
        return mark_safe("<a href='%s'>删除</a>"%self.get_delete_url(obj))

    def checkbox(self, obj=None, header=False):
        '''复选列'''
        if header:
            return mark_safe('<input id="choice" type="checkbox">')
        return mark_safe('<input class="choice_item" name="selected_pk" value="%s" type="checkbox"'%obj.pk)


    def new_list_play(self):
        '''获取所有展示列(默认情况下，会加入复选列，编辑列， 删除列)  [checkbox,"pk","name","age",edit ,deletes]'''
        temp = []
        temp.append(ModelXadmin.checkbox)
        temp.extend(self.list_display)
        if not self.list_display_links:
            temp.append(ModelXadmin.edit)
        temp.append(ModelXadmin.deletes)
        return temp

    def new_actions(self):
        temp = []
        temp.append(ModelXadmin.patch_delete)
        temp.extend(self.actions)
        return temp

    def get_modelform_class(self):
        if not self.modelform_class:
            from django.forms import ModelForm
            class ModelFormTemp(ModelForm):
                class Meta:
                    model = self.model
                    fields = "__all__"
                    labels = {}
            return ModelFormTemp
        else:
            return self.modelform_class


    def get_search_conditon(self, request):
        key_word = request.GET.get('q', "")
        self.key_word = key_word  #用于前端查询后保留关键字

        #由于search_field字段是字符串，必须用 支持字符串形式构造Q
        search_connection = Q()
        if key_word:
            search_connection.connector = "or"
            for search_field in self.search_fields:
                #__contains 支持模糊匹配
                search_connection.children.append((search_field + "__contains", key_word))
        return search_connection

    def get_filter_condition(self, request):
        filter_condition = Q()  #条件之间默认与关系

        for filter_field, val in request.GET.items():
            if filter_field not in ['page', 'q']:
                filter_condition.children.append((filter_field, val))
        return filter_condition


#定义  处理展示页面逻辑 类
class ShowList(object):

    def __init__(self, data_list, admin_config, request):
        self.data_list = data_list
        self.config = admin_config
        self.request = request

    @property
    def current_page_data(self):
        current_page = int(self.request.GET.get("page", 1))
        full_path = self.request.get_full_path()
        paginator = Paginator(self.data_list, 10, full_path, 11)
        try:
            data = paginator.page(current_page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        except NoDataPage:
            data = paginator.empty_page
        return data

    def page_html(self):
        return self.current_page_data.bulid_page_number_html()

    def header_list(self):
        header_list = []
        for field in self.config.new_list_play():
            if callable(field):  #自定义函数
                val = field(self.config, header=True)
            else:
                if field == '__str__':  #默认没配置情况，就显示表名大写
                    val = self.config.model._meta.model_name.upper()
                else:
                    val = self.config.model._meta.get_field(field).verbose_name
            header_list.append(val)
        return header_list

    def body_list(self):
        new_data_list = []
        for obj in self.current_page_data:
            row_data = []
            for field in self.config.new_list_play():
                if callable(field): #自定义函数
                    val = field(self.config, obj)
                else:
                    try:
                        field_obj = self.config.model._meta.get_field(field)
                        if isinstance(field_obj, ManyToManyField):
                            ret = getattr(obj, field).all()
                            t = []
                            for instance in ret:
                                t.append(str(instance))
                            val = ','.join(t)
                        else:
                            if field_obj.choices: #无choices属性，比如：CharField返回空列表
                                val = getattr(obj, 'get_' + field + '_display')
                            else:
                                val = getattr(obj, field)

                            if field in self.config.list_display_links:
                                val = mark_safe("<a href='%s'>%s</a>"%(self.config.get_change_url(obj), val))
                    except Exception as e:
                        val = getattr(obj, field)
                row_data.append(val)

            new_data_list.append(row_data)
        return new_data_list

    def get_action_list(self):
        temp = []
        for action in self.config.new_actions():
            temp.append(
                {
                    "name" : action.__name__,
                    "desc" : action.short_description
                }
            ) #  [{"name":""patch_init,"desc":"批量初始化"}]

        return temp

    def get_filter_linktags(self):
        '''
        获取filter点击项:
            筛选字段名:（筛选值id，筛选值）
                （一对多和多对多时，获取关联表里的所有值）
                (普通字段就当前表所有值)
        '''
        link_dic = {}

        for filter_field in self.config.list_filter:
            params = copy.deepcopy(self.request.GET)
            cid = self.request.GET.get(filter_field, 0)  #用于判断活动点击项
            filter_field_obj = self.config.model._meta.get_field(filter_field)

            '''取值为什么分两种情况？'''
            #关联表模型 字段对象.rel.to取到
            if isinstance(filter_field_obj, ForeignKey) or isinstance(filter_field_obj, ManyToManyField):
                filter_data_list = filter_field_obj.related_model.objects.all()
            else:
                filter_data_list = self.config.model.objects.all().values("pk", filter_field)

            temp = []
            #处理全部标签
            if params.get(filter_field):
                # 如果当前筛选项有值，说明全部就不是当前活动项，而且如果点击全部时，该字段筛选值不保留的，需删除
                del params[filter_field]
                temp.append("<a href='?%s'>全部</a>"%params.urlencode())
            else:
                temp.append("<a class='active' href='#'>全部</a>")

            #处理数据标签
            for obj in filter_data_list:
                if isinstance(filter_field_obj, ForeignKey) or isinstance(filter_field_obj, ManyToManyField):
                    pk = obj.pk
                    text = str(obj)
                    params[filter_field] = pk  #一对多和多对多时，通过id来筛选
                else:
                    pk = obj.get("pk")
                    text = obj.get(filter_field)
                    params[filter_field] = text  #普通字段通过显示值来筛选

                #确定是否为活动项
                _url = params.urlencode()
                if cid == str(pk) or cid == text:
                    link_tag = "<a class='active' href='?%s'>%s</a>"%(_url, text)
                else:
                    link_tag = "<a href='?%s'>%s</a>"%(_url, text)
                temp.append(link_tag)
            link_dic[filter_field] = temp
        return link_dic


#定义注册类
class XadminSite(object):
    def __init__(self):
        self._registry={}

    def register(self, model, xadmin_class=None):
        if not xadmin_class:
            xadmin_class = ModelXadmin
        self._registry[model] = xadmin_class(model, self)

    @property
    def urls(self):
        return self.get_urls(), None, None

    def get_urls(self):
        temp = []
        for model, xadmin_class_obj in self._registry.items():
            model_name = model._meta.model_name
            app_label = model._meta.app_label
            temp.append(
                url(r"^%s/%s/"%(app_label, model_name), xadmin_class_obj.curd_urls)
            )
        return temp


site = XadminSite()