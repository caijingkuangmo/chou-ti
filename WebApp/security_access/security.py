# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import views
from flask import request
from .APIConfigs import api_settings
from .errors import exceptions

class SecurityView(views.MethodView):

    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
    throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
    throttle_rates = api_settings.DEFAULT_THROTTLE_RATES

    def __init__(self):
        self.authenticators = self.get_authenticators() or ()
        self._authenticator = None
        super(SecurityView, self).__init__()

    def dispatch_request(self, *args, **kwargs):
        try:
            self.initial(*args, **kwargs)
        except exceptions.APIException as e:
            import json
            return json.dumps({'status_code':e.status_code, 'default_detail':e.detail, 'default_code':e.code})

        meth = getattr(self, request.method.lower(), None)
        # If the request method is HEAD and we don't have a handler for it
        # retry with GET.
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)
        assert meth is not None, 'Unimplemented method %r' % request.method
        return meth(*args, **kwargs)

    def initial(self,*args, **kwargs):
        try:
            self.perform_authentication
            self.check_permissions
            self.check_throttles
        except exceptions.APIException as e:
            raise

    @property
    def perform_authentication(self):
        for authenticator in self.authenticators:
            try:
                user_auth_tuple = authenticator.authenticate(self)
            except exceptions.APIException as e:
                self._not_authenticated()
                raise

            if user_auth_tuple is not None:
                self.user, self.auth = user_auth_tuple
                self._authenticator = authenticator
                return

        self._not_authenticated()


    @property
    def check_permissions(self):
        for permission in self.get_permissions():
            if not permission.has_permission(self):
                self.permission_denied(
                    message=getattr(permission, 'message', None)
                )

    def get_authenticators(self):
        return [auth() for auth in self.authentication_classes]


    @property
    def check_throttles(self):
        for throttle in self.get_throttles():
            if not throttle.allow_request(self):
                raise exceptions.Throttled("访问太频繁")


    def permission_denied(self, message=None):
        if self.authenticators:
            self.perform_authentication
            if not self._authenticator:
                raise exceptions.NotAuthenticated()
        raise exceptions.PermissionDenied(detail=message)

    def _not_authenticated(self):
        self._authenticator = None

    def get_permissions(self):
        return [permission() for permission in self.permission_classes]

    def get_throttles(self):
        return [throttle() for throttle in self.throttle_classes]


