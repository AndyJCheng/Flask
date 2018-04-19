#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2018/3/29 22:16
# @Author : Andy C
# @File   : config.py
# dialect+driver://username:password@host:port/database
DEBUG = True
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_migrate'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
