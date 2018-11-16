# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from rbac import models
from Xadmin.service.xadmin import site, ModelXadmin

class UserConfig(ModelXadmin):
    list_display = ['name', 'pwd', 'roles']

site.register(models.User, UserConfig)


class RoleConfig(ModelXadmin):
    list_display = ['title']

site.register(models.Role, RoleConfig)


class PermissionGroupConfig(ModelXadmin):
    list_display = ['title']

site.register(models.PermissionGroup, PermissionGroupConfig)


class PermissionConfig(ModelXadmin):
    list_display = ['title', 'url', 'action', 'group']

site.register(models.Permission, PermissionConfig)

