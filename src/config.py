import os

class Config(object):

    API_URL  = 'https://pokeapi.co/api/v2/pokemon/'
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
 
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
    BCRYPT_LOG_ROUNDS = 4  
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False  
