#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: migratemange.py
@time: 2018/4/18 23:20
flask_migrate can auto map to database after updating column every time,
rather than delete table,then create all.
@how to use? init migrate upgrade
models-->migrate-->database
1. init(initialize a migration env,only execute once )
2. migrate(generating a migration file from model)
3. upgrade(mapping into database from migration file)
"""
from flask_script import Manager
from demo import app
from models import User
from flask_migrate import Migrate, MigrateCommand
from exts import db


manger = Manager(app)
# 1. flask_migrate must bind app and db
migrate = Migrate(app, db)
# 2. add MigrateCommand to manger
manger.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manger.run()
