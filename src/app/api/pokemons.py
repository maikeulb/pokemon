import sys
from flask import jsonify, request
from app.api import api
from app.api.errors import bad_request
import requests

@api.route('/pokemons')
def get_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon/'
    data = requests.get(url).json()
    return jsonify(data), 200


@api.route('/pokemons/<id>', methods=['GET'])
def get_pokemon(id):
    url = 'https://pokeapi.co/api/v2/pokemon/' + id
    data = requests.get(url).json()

    pokemon = {
        'id': data['id'],
        'name': data['name'],
        'height': data['weight'],
        'weight': data['weight'],
        'abilities': [ability['ability']['name'] for ability in data['abilities']]
    }

    return jsonify(pokemon), 200
