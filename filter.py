#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: filter.py
@time: 2018/4/3 22:53
@desc: 把原始的变量经过处理展示出来，作用对象是变量
@usage: {{ val | default('xxxxx') }}   { val | length }}
http://www.bjhee.com/jinja2-filter.html
"""
from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    picture = 'https://img-ads.csdn.net/2018/201803011427162291.png'
    contents = [
            {
                'name': 'a',
                'author': 'adf',
                'price': 'aasfasdf'
            },
            {
                'name': 'a',
                'author': 'adf',
                'price': 'aasfasdf'
            }
        ]
    return render_template('index2.html', contents=contents)


if __name__ == '__main__':
    app.run()
