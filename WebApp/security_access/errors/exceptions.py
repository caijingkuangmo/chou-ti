# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from .status import *

class APIException(Exception):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'
    default_code = 'error'

    def __init__(self, detail=None, code=None):
        self.detail = self.default_detail if detail is None else detail
        self.code = self.default_code if code is None else code

class AuthenticationFailed(APIException):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = 'Incorrect authentication credentials.'
    default_code = 'authentication_failed'



class NotAuthenticated(APIException):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = 'Authentication credentials were not provided.'
    default_code = 'not_authenticated'


class PermissionDenied(APIException):
    status_code = HTTP_403_FORBIDDEN
    default_detail = 'You do not have permission to perform this action.'
    default_code = 'permission_denied'


class Throttled(APIException):
    status_code = HTTP_429_TOO_MANY_REQUESTS
    default_detail = 'Request was throttled.'
    default_code = 'throttled'








