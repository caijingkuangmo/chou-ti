# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from exchange import db
from security_access import security, errors
from security_access.default_class import *
import config

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(config.TestingConfig)
db.init_app(app)

class User(db.Model):
    __tablename__ = 'app01_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    pwd = db.Column(db.String(32))
    # token = db.relationship("Token", backref="user", uselist=False)
    def __repr__(self):
        return self.name

class Token(db.Model):
    __tablename__ = 'app01_token'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(128))
    user_id = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    def __repr__(self):
        return self.token

class VipPermission(BasePermission):
    message = 'vip assess'
    def has_permission(self, view):
        user_type = request.args.get("user_type", None)
        if user_type == "vip":
            return True
        return False

class Authentication(BaseAuthentication):
    def authenticate(self, view):
        token = request.args.get("token", None)
        token_obj = db.session.query(Token).filter_by(token=token).first()
        if not token_obj:
            raise errors.AuthenticationFailed('认证失败')
        else:
            return token_obj.user_id, token_obj.token


class IndexView(security.SecurityView):
    methods = ['GET', 'POST']
    decorators = []
    authentication_classes = [Authentication,]
    permission_classes = [VipPermission,]
    throttle_classes = [IPThrottling,]
    # throttle_rates = {
    #         "visit_rate":"20/60/120"
    #     }

    def get(self):
        return 'Index.GET'

    def post(self):
        return 'Index.POST'


app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))

if __name__ == '__main__':
    app.run()