# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __init__ import db
# from __init__ import create_app


class UserInfo(db.Model):

    __tablename__ = 'userinfo'

    nid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    ctime = db.Column(db.TIMESTAMP)

    __table_args__ = (
        db.Index('ix_user_pwd', 'username', 'password'),
        db.Index('ix_email_pwd', 'email', 'password'),
    )

class NewsType(db.Model):

    __tablename__ = 'newstype'

    nid = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(32))

class News(db.Model):

    __tablename__ = 'news'

    nid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_info_id = db.Column(db.Integer, db.ForeignKey("userinfo.nid"))
    news_type_id = db.Column(db.Integer, db.ForeignKey("newstype.nid"))
    ctime = db.Column(db.TIMESTAMP)
    title = db.Column(db.String(32))
    url = db.Column(db.String(128))
    content = db.Column(db.String(150))

class Favor(db.Model):

    __tablename__ = 'favor'

    nid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_info_id = db.Column(db.Integer, db.ForeignKey('userinfo.nid'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.nid'))
    ctime = db.Column(db.TIMESTAMP)

    __table_args__ = (
        db.UniqueConstraint('user_info_id', 'news_id', name='uix_uid_nid'),
    )


class Comment(db.Model):
    __tablename__ = 'comment'

    nid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 评论者id
    user_info_id = db.Column(db.Integer, db.ForeignKey("userinfo.nid"))
    # 评论的信息id
    news_id = db.Column(db.Integer, db.ForeignKey("news.nid"))
    # 如果为None，就是评论文章，如果是数字就是回复某个人
    reply_id = db.Column(db.Integer, db.ForeignKey("comment.nid"), nullable=True, default=None)
    # 顶一下
    up = db.Column(db.Integer)
    # 踩一下
    down = db.Column(db.Integer)
    # 创建时间
    ctime = db.Column(db.TIMESTAMP)
    # 发表设备：手机，电脑，苹果....
    device = db.Column(db.String(32))
    # 发表内容
    content = db.Column(db.String(150))


class SendCode(db.Model):

    __tablename__ = "sendcode"

    # 注册时验证码信息
    nid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(32), index=True)
    code = db.Column(db.String(4))
    status = db.Column(db.Integer)  #状态码，0表示未注册，1成功，2拉黑
    # 验证码的有效时间
    stime = db.Column(db.TIMESTAMP)  # 发送时间


# app = create_app()
# def create_all():
#     with app.app_context():
#         db.create_all()
#
# def drop_all():
#     with app.app_context():
#         db.drop_all()
#
#
# create_all()
