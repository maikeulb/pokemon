from redis import StrictRedis
import requests
import requests_cache
from urllib.parse import urlparse

# redis_url = app.config.get('REDIS_URL')
# redis_url= "redis://172.0.17.5://localhost:6379"
# if redis_url:
    # url = urlparse(redis_url)
    # cache = Redis(host=url.hostname, port=url.port, password=url.password)

cache = StrictRedis(
    host="localhost",
    port=6379,
    db=0)

