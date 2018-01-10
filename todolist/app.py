#encoding:utf8

from flask import Flask
from controllers import blueprints
from configs import config
from exts import db

def create_app(config_name=None):
    if config_name is None:
        config_name = 'default'

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    for bp in blueprints:
        app.register_blueprint(bp)

    return app