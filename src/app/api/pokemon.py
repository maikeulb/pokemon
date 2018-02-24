from flask import jsonify, request
from app import db
from app.models import City
from app.api import api
from app.api.errors import bad_request
from sqlalchemy import func


@api.route('/pokemon', defaults={'search_query': None, 'order_by': None}, methods=['GET'])
def get_pokemons(search_query, order_by):
    search_query = request.args.get('search_query')
    order_by = request.args.get('order_by')
    city_query = City.query

    if search_query:
        city_query = \
        city_query.filter(func.lower(City.name).contains(func.lower(search_query)) | \
                          func.lower(City.state).contains(func.lower(search_query)))

    if order_by == 'name':
        city_query = city_query.order_by('name')

    if order_by == 'state':
        city_query = city_query.order_by('state')

    # page = request.args.get('page', 1, type=int)
    # per_page = min(request.args.get('per_page', 10, type=int), 100)
    # data = City.to_collection_dict(city_query, page, per_page,
    #                                'api.get_cities')
    # return jsonify(data), 200


@api.route('/cities/<int:id>', methods=['GET'])
def get_pokemon(id):
    data = City.query.get_or_404(id).to_dict()
    return jsonify(data), 200
