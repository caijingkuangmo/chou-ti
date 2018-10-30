# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from .settings import settings
from importlib import import_module

def perform_import(val, setting_name):
    '''

    :param val: 配置类  可能是字符串，也可能是列表
    :param setting_name: 配置项名称
    :return:
    '''
    if val is None:
        return None
    elif isinstance(val, str):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val

def import_from_string(val, setting_name):
    try:
        module_path, class_name = val.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        msg = "无法导入setting_name为%s下的%s,错误信息为%s:%s"%(setting_name,val,e.__class__.__name__,e)
        raise ImportError(msg)

DEFAULTS = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'security_access.default_class.UsernameAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'security_access.default_class.AllowAny',
    ),
    'DEFAULT_THROTTLE_CLASSES': (),
    "DEFAULT_THROTTLE_RATES": {
        "visit_rate":"5/60/60"
    }
}

class APISettings(object):
    def __init__(self, user_settings=None, defaults=None):
        # if user_settings:
        #     self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, "SECURITY", {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting:'%s'"%attr)

        try:
            val = self.user_settings[attr]
        except KeyError:
            val = self.defaults[attr]

        if attr in DEFAULTS:
            val = perform_import(val, attr)
        setattr(self, attr, val)
        return val



api_settings = APISettings(None, DEFAULTS)