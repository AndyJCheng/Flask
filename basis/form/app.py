#!/usr/bin/env python
# encoding: utf-8

"""
@author: Andy Cheng
@license: Apache Licence 
@file: app.py
@time: 2018/12/21 22:16
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'welcome back'


@app.route('/login')
def login():
    return render_template('login.html')

