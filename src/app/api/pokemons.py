from flask import jsonify, request
from app.api import api
from app.api.errors import bad_request
from sqlalchemy import func


@api.route('/')
def get_pokemons()

	url = 'https://pokeapi.co/api/v2/pokemon/'
	api_response = requests.get(url)

    return jsonify(data), 200


@api.route('/<int:id>', methods=['GET'])
def get_pokemon(id):
	url = 'https://pokeapi.co/api/v2/pokemon/' + id

	api_response = requests.get(url)

    return jsonify(data), 200
