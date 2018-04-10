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


class Articals(db.Model):
    __tablename__ = 'Articals'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.TEXT, nullable=False)


db.create_all()


@app.route('/')
def index():
    # artical1 = Articals(title='aa', content='fafdsfasf')
    # db.session.add(artical1)
    # db.session.commit()

    # artical1 = Articals.query.filter(Articals.title == 1).all()[0]
    # artical1 = Articals.query.filter(Articals.title == 'aa').first()
    # artical1.title = 'new title'
    # db.session.commit()

    artical1 = Articals.query.filter(Articals.title == 'new title').first()
    db.session.delete(artical1)
    db.session.commit()
    return 'hello'


if __name__ == '__main__':
    app.run(port=555)
