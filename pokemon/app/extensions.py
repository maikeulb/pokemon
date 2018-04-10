from redis import StrictRedis
from config import Config

redis = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)
