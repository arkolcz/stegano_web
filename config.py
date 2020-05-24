from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config: 
    SECRET_KEY = environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application")

    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    if not SESSION_COOKIE_NAME:
        raise ValueError("No SESSION_COOKIE_NAME set for Flask application")

    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    if not STATIC_FOLDER:
        raise ValueError("No STATIC_FOLDER set for Flask application")

    UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')
    if not UPLOAD_FOLDER:
        raise ValueError("No UPLOAD_FOLDER set for Flask application")   
    
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
    if not TEMPLATES_FOLDER:
        raise ValueError("No TEMPLATES_FOLDER set for Flask application")

class ProdConfig(Config):
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    DEBUG = True
    TESTING = True