#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: demo.py
@time: 2018/4/17 22:51
"""
from flask import Flask
from exts import db
from models import UserTest
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    app.run()
