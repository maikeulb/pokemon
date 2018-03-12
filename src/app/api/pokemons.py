import os
import time
import sys
from flask import jsonify, current_app, request, g
from app.api import api
import requests
import time
import json
from app.extensions import redis


@api.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)


@api.route('/pokemons', defaults={'limit': None, 'offset': None})
def get_pokemons(limit, offset):

    url = current_app.config['API_URL']
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    if limit is not None and offset is None:
        url = url + '?limit=' + limit

    if limit is None and offset is not None:
        url = url + '?offset=' + offset

    if limit is not None and offset is not None:
        url = url + '?limit=' + limit + '&offset=' + offset

    cache_key = '{}_{}'.format(limit, offset)

    serialized_pokemons = redis.get(cache_key)
    if not serialized_pokemons:
        data = requests.get(url).json()
        pokemons = {
            'count': data['count'],
            'results': data['results']
        }
        serialized_pokemons = json.dumps(pokemons)
        redis.set(cache_key, serialized_pokemons)
        t = request.values.get('t', 0)
        print('Time without cache {} ms'.format(
            g.request_time()), sys.stdout)
        return jsonify(pokemons), 200

    deserialized_pokemons = json.loads(serialized_pokemons.decode('utf-8'))
    t = request.values.get('t', 0)
    print('Time with cache {} ms'.format(g.request_time()), sys.stdout)
    return jsonify(deserialized_pokemons), 200


@api.route('/pokemons/<id>', methods=['GET'])
def get_pokemon(id):
    url = current_app.config['API_URL'] + id

    cache_key = '{}'.format(id)
    serialized_pokemon = redis.get(cache_key)
    if not serialized_pokemon:
        data = requests.get(url).json()
        pokemon = {
            'id': data['id'],
            'name': data['name'],
            'height': data['weight'],
            'weight': data['weight'],
            'abilities': [ability['ability']['name'] for ability in data['abilities']]
        }
        serialized_pokemon = json.dumps(pokemon)
        redis.set(cache_key, serialized_pokemon)
        t = request.values.get('t', 0)
        print('Time without cache {} ms'.format(
            g.request_time()), sys.stdout)
        return jsonify(pokemon), 200

    deserialized_pokemon = json.loads(serialized_pokemon.decode('utf-8'))
    t = request.values.get('t', 0)
    print('Time with cache {} ms'.format(g.request_time()), sys.stdout)
    return jsonify(deserialized_pokemon), 200
