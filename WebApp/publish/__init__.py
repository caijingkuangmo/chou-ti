# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint('publish', __name__)
api = Api(blueprint)

from . import resources