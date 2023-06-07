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
    
    fav_data = []

    for favorites_planets in favoritesPlanets:
        fav_data.append(favorites_planets.serialize())

    for favorites_characters in favoritesCharacters:
        fav_data.append(favorites_characters.serialize())

    print(fav_data)
    return jsonify(fav_data)


@api.route('/favorite/planet/<int:planet_id>/<int:user_id>', methods=['POST'])
def post_favorites(planet_id, user_id):
    user = User.query.get(user_id)
    if user:
        favorite = Favorites_planets(user_id=user.id, planet_id=planet_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite planet added successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404


@api.route('/favorite/character/<int: character_id>/<int:user_id>', method=['post'])
def post_character(character_id, user_id):
    user = User.query.get(user_id)
    if user: 
        favorite = Favorites_characters(user_id=user.id, character_id=character_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite character added successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404


@api.route('/favorite/planet/<int:planet_id>/<int:user_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id, user_id):
    user = User.query.get(user_id)
    if user:
        favorite = Favorites_planets.query.filter_by(user_id=user.id, planet_id=planet_id).first()
        if favorite:
            db.session.delete(favorite)
            db.session.commit()
            return jsonify({'message': 'Favorite planet deleted successfully'})
        else:
            return jsonify({'message': 'Favorite planet not found'}), 404
    else:
        return jsonify({'message': 'User not found'}), 404


@api.route('/favorite/character/<int:character_id>/<int:user_id>', methods=['DELETE'])
def delete_favorite_people(character_id, user_id):
    user = User.query.get(user_id)
    if user:
        favorite = Favorites_characters.query.filter_by(user_id=user.id, character_id=character_id).first()
        if favorite:
            db.session.delete(favorite)
            db.session.commit()
            return jsonify({'message': 'Favorite people deleted successfully'})
        else:
            return jsonify({'message': 'Favorite people not found'}), 404
    else:
        return jsonify({'message': 'User not found'}), 404