#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: api.py
@time: 2018/8/8 21:49
"""
from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
