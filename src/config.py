import os

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(dotenv_path)


class Config(object):

    API_URL = 'https://pokeapi.co/api/v2/pokemon/'
    REDIS_HOST = os.getenv('REDIS_HOST', '172.17.0.5')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)

    DEVELOPMENT = False
    TESTING = False
    PRODUCTION = False
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DEBUG_TB_ENABLED = True


class ProductionConfig(Config):
    DATABASE_URI = ''
    PRODUCTION = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
