# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

def initial_session(user, request):
    '''
    把当前用户的所有权限注入request.session, 只需在登录成功时调用
    :param user:
    :param request:
    :return:
    '''
    permissions_list = user.roles.all().values(
        "permissions__url", "permissions__group_id", "permissions__action", "permissions__group__title"
    ).distinct()
    print('permissions_list', permissions_list)

    permission_dict = {}
    for permission_item in permissions_list:
        group_id = permission_item.get("permissions__group_id")
        if group_id not in permission_dict:
            permission_dict[group_id] = {
                "urls" : [permission_item['permissions__url'],],
                "actions" : [permission_item['permissions__action'],]
            }
        else:
            permission_dict[group_id]["urls"].append(permission_item["permissions__url"])
            permission_dict[group_id]["actions"].append(permission_item["permissions__action"])

    print('permission_dict', permission_dict)
    request.session['permission_dict'] = permission_dict

    # 注册菜单权限
    menu_permission_list = []
    for item in permissions_list:
        if item['permissions__action'] == "list":
            menu_permission_list.append(
                (item["permissions__url"], item["permissions__group__title"])
            )

    print('menu_permission_list', menu_permission_list)
    request.session["menu_permission_list"] = menu_permission_list