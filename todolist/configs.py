#encoding:utf8

import os
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config(object):
    SECRET_KEY = os.urandom(23)
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BABEL_DEFAULT_LOCALE = 'zh'
    BABEL_DEFAULT_TIMEZONE = 'CST'

class DevelopmentConfig(Config):
    DEBUT = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'todo.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'todo.sqlite')


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
