import time
import sys
from flask import jsonify, current_app, request
from app.api import api
from app.extensions import cache
# import redis
import requests
# import requests_cache
# redis_url= "redis://172.0.17.8://localhost:6379')"

# REDIS_HOST = os.getenv('FASTPASS_REDIS_HOST', '127.0.0.1')
# REDIS_PORT = os.getenv('FASTPASS_REDIS_PORT', 36379)
# REDIS_PASSWORD = os.getenv('FASTPASS_REDIS_PASSWORD', '')
# redis_conn = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

# redis_conn = redis.from_url(redis_url)
# requests_cache.install_cache('poke_cache', backend='redis',
                             # connection=redis_conn, expire_after=300)
# requests_cache.clear()
# print("filling cahce", sys.stdout)


# @cache.cached(timeout=50)
@api.route('/pokemons', defaults={'limit': None, 'offset': None})
def get_pokemons(limit, offset):
    url = current_app.config['API_URL']
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if limit is not None and offset is None:
        print('limit', sys.stdout)
        url = url + '?limit=' + limit
        print(url, sys.stdout)

    if limit is None and offset is not None:
        print('offset', sys.stdout)
        url = url + '?offset=' + offset
        print(url, sys.stdout)

    if limit is not None and offset is not None:
        url = url + '?limit=' + limit + '&offset=' + offset

    data = requests.get(url).json()

    response = {
        'count': data['count'],
        'results': data['results']
    }

    return jsonify(response), 200


@api.route('/pokemons/<id>', methods=['GET'])
def get_pokemon(id):
    url = current_app.config['API_URL'] + id
    data = requests.get(url).json()

    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['weight'],
        'weight': data['weight'],
        'abilities': [ability['ability']['name'] for ability in data['abilities']]
    }

    return jsonify(pokemon), 200
