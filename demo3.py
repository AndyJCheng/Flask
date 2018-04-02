#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2018/4/2 23:03
# @Author : Andy C
# @File   : demo3.py
from flask import Flask, render_template
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/home/')
def home():
    user = {
        'name': 'andy',
        'age': 25
    }
    return render_template('index1.html', user=user)


if __name__ == '__main__':
    app.run()
