#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2018/3/29 22:48
# @Author : Andy C
# @File   : demo2.py

from flask import Flask, url_for, redirect, render_template
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def home():
    return redirect(url_for('login'))
    return 'this is home page'


@app.route('/login/')
def login():
    class Person:
        name = 'dfasfs'
        age = 22
    p = Person()
    content = {
        'user': 'andy',
        'age': 25,
        'person': p,
        'websites': {
            'baidu': 'baidu.com'
        }
    }
    return render_template('index.html', **content)


@app.route('/question/<id>')
def question(id):
    if id == '1':
        return 'this is question page'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()


