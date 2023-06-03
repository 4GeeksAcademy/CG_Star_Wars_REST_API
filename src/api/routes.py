"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/characters', methods=['GET'])
def get_characters():

    characters = Character.query.all()

    character_data = []
    for character in characters:
        character_data.append(character.serialize())
    return jsonify(character_data)


