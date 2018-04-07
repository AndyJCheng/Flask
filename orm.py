#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.6
@author: andy cheng
@file: orm.py
@usage:flask-SQLALchemy is a ORM frame,operate DB is like object(table-class)
pip install pymysql
pip install flask_SQLAlchemy
@time: 2018/4/6 22:44
"""
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
db.create_all()


@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    app.run()


