import os
import tempfile
from flask import Flask, flash, request, redirect, url_for, render_template, session, send_file, Response
from flask import current_app as app
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def extension_allowed(file):
    return '.' in file and \
        file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def encrypt_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and extension_allowed(file.filename):
            filename = secure_filename(file.filename)
            #TODO: Run ecryption file

    return render_template('index.html')
