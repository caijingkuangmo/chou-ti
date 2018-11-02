# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from app01 import models
from Xadmin.service.xadmin import site, ModelXadmin

class PublishConfig(ModelXadmin):
    list_display = ['name', 'city', 'email']
    list_display_links = ['name']
    search_fields = ['name', 'city']

    def patch_change(self, request, queryset):
        queryset.update(city='宜春')
    patch_change.short_description = "批量修改"
    actions = [patch_change]


site.register(models.Author)
site.register(models.Publish, PublishConfig)

class BookConfig(ModelXadmin):
    list_display = ["title","price","publishDate","publish","authors"]
    list_display_links = ["title"]
    # modelform_class=BookModelForm
    search_fields=["title","price"]

    def patch_init(self, request, queryset):
        print(queryset)
        queryset.update(price=123)
    patch_init.short_description = "批量初始化"

    actions = [patch_init]
    list_filter=["title","publish","authors",]

site.register(models.Book, BookConfig)