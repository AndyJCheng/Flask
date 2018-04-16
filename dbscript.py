#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: dbscript.py
@time: 2018/4/16 23:10
"""
from flask_script import Manager
DBManger = Manager()


@DBManger.command
def init():
    return 'DB inital'


@DBManger.command
def migrate():
    return 'DB migrate successfully'
