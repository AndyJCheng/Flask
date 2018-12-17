#!/usr/bin/env python
# encoding: utf-8
"""
@author: Andy Cheng
@license: Apache Licence 
@file: sample.py
@time: 2018/12/18 0:01
"""
from flask import Flask

app = Flask(__name__)

# bind multiple url to view method


@app.route('/greet', defaults={'name': 'programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>hello, %s</h1>' % name

#
# if __name__ == '__main__':
#     app.run()
# app.run()---> flask run
# how to startup app: 1 set FLASK_APP=sample.py, 2 flask run(python -m flask run)
