#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: flaskscript.py
@desc: used to operate Flask by command, for example,
run development version server by command, config db,cron task.
@time: 2018/4/16 22:50
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)