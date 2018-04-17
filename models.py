#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: models.py
@time: 2018/4/17 23:02
"""
from exts import db


class UserTest(db.Model):
    __tablename__ = 'UserTest'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=True)


