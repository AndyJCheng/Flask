#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: getpost.py
@time: 2018/4/26 23:17
g: g object record user all data, only work in one request
"""
from flask import Flask, render_template
from flask import request, g, redirect, session, url_for
from utils import login_log
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    # return render_template('getpost.html')
    return render_template('context1.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'andy' and password == '55':
            # g.username = username
            # login_log()
            session['username'] = username
            return 'login successfully'
        else:
            return 'incorrect username or password'


@app.route('/search/')
def search():
    return request.args.get('q')


@app.route('/edit/')
def edit():
    # if hasattr(g, 'username'):
    #     return 'edit successfully'
    # else:
    #     return redirect(url_for('login'))
    return render_template('edit.html')


@app.before_request
def before():
    if session.get('username'):
        g.username = session.get('username')


@app.context_processor
def my_context():
    # username = session.get('username')
    # if username:
    #     return {'username': username}
    return {'username': 'andy'}


if __name__ == '__main__':
    app.run(debug=True)
