import sys
from flask import jsonify, current_app, request
from app.api import api
import requests


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
