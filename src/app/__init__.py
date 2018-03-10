import config
import os
from flask import (
    Flask,
    request)
from app.api import api as api_bp
from app.extensions import cache, requests_cache

Config = eval(os.environ['FLASK_APP_CONFIG'])


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    register_extensions(app)
    return app

def register_blueprints(app):
    app.register_blueprint(api_bp, url_prefix='/api')
    return None

def register_extensions(app):
    requests_cache.install_cache('registers_cache', backend='redis', expire_after=300, connection=cache)
    return None
