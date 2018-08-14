#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: apiplus.py
@time: 2018/8/8 23:33
"""
from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app, prefix="/v1", title="user test", description="user CURD api")


@api.route("/users")
class UserApi(Resource):
    def get(self):
        return {'user': '1'}


if __name__ == '__main__':
    app.run()
