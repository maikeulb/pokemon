import config
import os
from flask import (
    Flask,
    request)
from app import models
from app.api import api as api_bp

Config = eval(os.environ['FLASK_APP_CONFIG'])


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')
    return None
