# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from __init__ import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

'''
数据迁移命令
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
'''

manager.add_command('db', MigrateCommand)