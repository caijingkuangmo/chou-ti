# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get('https://www.baidu.com')
# print(driver.page_source)
#
# import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
# from sqlalchemy.engine.base import Engine
#
# engine = create_engine(
#     'mysql+pymysql://root:123@127.0.0.1:3306/t1?charset=utf8',
#     max_overflow=0,
#     pool_size=5,
#     pool_timeout=30,
#     pool_recycle=-1
# )
#
# Base = declarative_base()
#
# class Users(Base):
#     __tablename__ = 'users'
#
#     uid = Column(Integer, primary_key=True)
#     name = Column(String(32), index=True, nullable=False)
#     email = Column(String(32), unique=True)
#
#     __table_args__ = (
#         UniqueConstraint('uid', 'name', name='uix_uid_name'),
#         Index('ix_uid_name', 'name', 'email')
#     )
#
# class UserProfile(Base):
#     __tablename__ = 'userprofile'
#
#     uid = Column(Integer, primary_key=True)
#     job_number = Column(Integer, nullable=False, unique=True)
#     username = Column(String(32), nullable=False)
#     password = Column(String(256), nullable=False)
#     job_role = Column()
#
# class Role(Base):
#     __tablename__ = 'role'
#
#
# def init_db():
#     Base.metadata.create_all(engine)
#
# def drop_db():
#     Base.metadata.drop_all(engine)
#
# if __name__ == '__main__':
#     drop_db()
#     init_db()

import hashlib

m = hashlib.md5()
m.update(b"123456")
print(m.hexdigest())