#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: getpost.py
@time: 2018/4/26 23:17
g: g object record user all data, only work in one request
"""
from flask import Flask, render_template, request, g
from utils import login_log
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
        if username == 'andy' and password == '55':
            g.username = username
            login_log()
            return 'login successfully'
        else:
            return 'incorrect username or password'


@app.route('/search/')
def search():
    return request.args.get('q')


if __name__ == '__main__':
    app.run(debug=True)
