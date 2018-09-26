# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

from flask import Flask
from config import config
# from flask_sqlalchemy import SQLAlchemy
# from flask_login.login_manager import LoginManager
#
#
# db = SQLAlchemy()
# login_manager = LoginManager()
# login_manager.session_protection = 'strong'


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    # db.init_app(app)
    # login_manager.init_app(app)

    from account import blueprint as account_bp
    app.register_blueprint(account_bp, url_prefix='/account')

    return app
