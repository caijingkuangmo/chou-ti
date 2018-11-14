# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from django import template

register = template.Library()

@register.inclusion_tag("rbac/menu.html")
def get_menu(request):
    # 获取当前用户菜单栏权限
    menu_permission_list = request.session['menu_permission_list']
    return {"menu_permission_list" : menu_permission_list}