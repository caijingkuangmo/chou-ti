# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from werkzeug.utils import secure_filename
from datetime import datetime

from db import models
from __init__ import db

def publish_link_info(**kwargs):
    kwargs['ctime'] = datetime.utcnow()
    db.session.add(models.News.add(**kwargs))
    db.session.commit()
    db.session.close()
    return True

def publish_word_info(**kwargs):
    kwargs['ctime'] = datetime.utcnow()
    db.session.add(models.News.add(**kwargs))
    db.session.commit()
    db.session.close()
    return True

def publish_image_info(file, **kwargs):
    file_name = save_file(file)
    kwargs['fname'] = file_name
    kwargs['ctime'] = datetime.utcnow()
    db.session.add(models.News.add(**kwargs))
    db.session.commit()
    db.session.close()
    return True

def save_file(file):  #表中没有图片存储字段
    file = file['file']
    file_name = 'static/img/' + secure_filename(file.filename)
    file.save(file_name)
    return file_name
