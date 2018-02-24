import config
import os
from flask import (
    Flask,
    request)
from app.api import api as api_bp
from app.extensions import cache
# from flask_caching import Cache
# from flask.ext.cache import Cache

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
    # from redis import Redis
    import requests
    import requests_cache
    from urllib.parse import urlparse

    # redis_url = app.config.get('REDIS_URL')
    # if redis_url:
        # url = urlparse(redis_url)
        # cache = Redis(host=url.hostname, port=url.port, password=url.password)
    # else:
        # cache = Redis() # local dev default

    # requests_cache.install_cache('registers_cache', backend='redis', expire_after=300, connection=cache)
    requests_cache.install_cache('registers_cache', backend='sqlite', expire_after=300, connection=cache)

    return None
