#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2018/3/29 22:15
# @Author : Andy C
# @File   : demo1.py

from flask import Flask, url_for
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def test():
    """
    reverse url
    :return:
    """
    print(url_for('article', id=1))
    return 'hello flask'


@app.route('/article/<id>')
def article(id):
    return u"你的id是：%s" % id


if __name__ == '__main__':
    app.run()
