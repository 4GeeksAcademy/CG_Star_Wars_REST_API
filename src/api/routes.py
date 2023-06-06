"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Favorites_characters, Favorites_planets
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/characters', methods=['GET'])
def get_characters():

    characters = Character.query.all()

    character_data = []
    for character in characters:
        character_data.append(character.serialize())
    return jsonify(character_data)

@api.route('/character/<int:character_id>', methods=['GET'])
def get_character(character_id):

    character = Character.query.get(character_id)
    if character:
        return character.serialize()
    else:
        return "Character not found", 404

@api.route('/planets', methods=['GET'])
def get_planets():

    planets = Planet.query.all()

    planet_data = []
    for planet in planets:
        planet_data.append(planet.serialize())
    return jsonify(planet_data)

@api.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    planet = Planet.query.get(planet_id)
    if planet:
        return planet.serialize()
    else:
        return "Planet not found", 404


@api.route('/users', methods=['GET'])
def get_users():

    users = User.query.all()

    user_data = []
    for user in users:
        user_data.append(user.serialize())
    return jsonify(user_data)

@api.route('/favorites', methods=['GET'])
def get_favorites(): 

    favoritesPlanets = Favorites_planets.query.all() 
    favoritesCharacters = Favorites_characters.query.all()
    
    fav_planets_data = []
    fav_characters_data = []

    for favorites_planets in favoritesPlanets:
        fav_planets_data.append(favorites_planets.serialize())

    for favorites_characters in favoritesCharacters:
        fav_characters_data.append(favorites_characters.serialize())

    return jsonify({
        'fav_planets': fav_planets_data,
        'fav_characters': fav_characters_data
    })