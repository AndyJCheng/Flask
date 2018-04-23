#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: demo.py
@time: 2018/4/20 22:45
flask session working mechanism:
encrypting the data into session,
then save the session to cookie.
saving the server resource,because
put it into client.
"""
from flask import Flask, session
import os
from datetime import timedelta
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
# config session timeout time
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/')
def index():
    session['username'] = 'andy cheng'
    # session timeout after close browser
    # session.permanent = True, keep session 31 days
    session.permanent = True
    return 'session'


@app.route('/get/')
def get():
    return session.get('username')


@app.route('/delete/')
def delete():
    # session.get() avoid exception
    print(session.get('username'))
    # session.clear(),clear all information in session
    session.pop('username')
    print(session.get('username'))
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
