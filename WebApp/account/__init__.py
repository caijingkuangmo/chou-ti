# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint('account', __name__)

api = Api(blueprint)

from account import resources