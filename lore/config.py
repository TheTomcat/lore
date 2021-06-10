import os
import logging
from datetime import timedelta
# from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir,'.env'))

class Config(object):
    SERVER_NAME = '127.0.0.1:5000'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'l;aiksusehrgvfpi7q3b4pi'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # https://blog.miguelgrinberg.com/post/cookie-security-for-flask-applications

    SESSION_COOKIE_SECURE = False # CHANGE TO TRUE FOR DEPLOYMENT
    REMEMBER_COOKIE_SECURE = False # As above

    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    HASHID_SALT = os.environ.get('HASHIDS_SALT') or 'not very secure'

class TestConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "test.db")}'