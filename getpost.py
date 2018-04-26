#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: getpost.py
@time: 2018/4/26 23:17
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('getpost.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        return 'ok'


@app.route('/search/')
def search():
    return request.args.get('q')


if __name__ == '__main__':
    app.run(debug=True)
