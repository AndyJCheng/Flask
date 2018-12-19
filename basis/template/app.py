#!/usr/bin/env python
# encoding: utf-8
"""
@author: Andy Cheng
@license: Apache Licence 
@file: app.py
@time: 2018/12/19 23:30
"""
from flask import Flask, render_template
app = Flask(__name__)

user = {
    'username': 'andy cheng',
    'bio': 'a boy who loves movies and music',
}

movies = [
    {'name': 'my neiphbor totoro', 'year': '19888'},
    {'name': 'three colours trilogy', 'year': '1993'},
    {'name': 'forrest gump', 'year': '1994'}
]


@app.route('/')
def index():
    return 'hello flask'


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)

