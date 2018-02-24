import sys
from flask import jsonify, current_app
from app.api import api
import requests


@api.route('/pokemons')
def get_pokemons():
    url = current_app.config['API_URL']
    data = requests.get(url).json()
    return jsonify(data), 200


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
