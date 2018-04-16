#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: manage.py
@usage: python manger.py runserver, python manger.py init(migrate)
@time: 2018/4/16 23:00
"""
from flask_script import Manager
from flaskscript import app
from dbscript import DBManger

manger = Manager(app)


@manger.command
def runserver():
    return 'the server running'


manger.add_command('db', DBManger)
if __name__ == '__main__':
    manger.run()
