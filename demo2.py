#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2018/3/29 22:48
# @Author : Andy C
# @File   : demo2.py

from flask import Flask, url_for, redirect
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def home():
    return redirect(url_for('login'))
    return 'this is home page'


@app.route('/login/')
def login():
    return 'this is login page'


@app.route('/question/<id>')
def question(id):
    if id == '1':
        return 'this is question page'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
