#!/usr/bin/env python
# encoding: utf-8
"""
@author: andy cheng
@license: Apache Licence 
@file: fileupload.py
@time: 2018/7/28 23:32
"""
from flask import request, redirect, url_for, Flask, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'html'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload():
    folder = r'D:\googledownload'
    result = ''
    if request.method == 'POST':
        file = request.files['file']
        # if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(folder, filename)
        file.save(upload_path)
        if os.path.exists(upload_path):
            result = 'upload successfully'
        else:
            result = 'upload failed'
        # return redirect(url_for('upload'))
    return render_template('fileupload.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
