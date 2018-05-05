#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: utils.py
@time: 2018/5/5 23:20
"""
from flask import g


def login_log():
    print('your username is %s' % g.username)