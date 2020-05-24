import os
import tempfile
import stegano
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
        
        if 'text' not in request.form:
            return redirect(request.url)
        text = request.form['text']
        
        if text == '':
            return redirect(request.url)

        if file and extension_allowed(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            stegano.encrypt(file_path,text)

    return render_template('index.html')

#TODO: Add information for a user with error/exception
#TODO: Think of better way to store images. Ideally processing images without saving them on a server.
#TODO: Move stegano.py from project root tp /app
#TODO: Decryption algorithm
#TODO: Fix encrypted image name.
#TODO: Add file size cap for image upload.
