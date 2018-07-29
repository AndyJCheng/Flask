#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: fileupload_improve.py
@time: 2018/7/29 21:40
"""
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import render_template, request, url_for, Flask, redirect, abort
import os

app = Flask(__name__)
app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES

photos = UploadSet('PHOTO')
configure_uploads(app, photos)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return redirect(url_for('upload'))
    return render_template('upload.html')


@app.route('/photo/<name>')
def show(name):
    if name is None:
        abort(404)

    url = photos.url(name)
    return render_template('show.html', url=url, name=name)


@app.errorhandler(404)
def error(e):
    return 'not found'


if __name__ == '__main__':
    app.run(debug=True)
