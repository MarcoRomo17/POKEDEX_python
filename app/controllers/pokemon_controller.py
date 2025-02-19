from flask import Blueprint, request, jsonify #secciona el servidor en urls
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemons",__name__, url_prefix="/pokemons")#Carpeta u endpoint

pokemons= ModelFactory.get_model("pokemons")

@bp.route("/getAll", methods=["GET"])
def get_ALL():
    pokemons_all= pokemons.find_all()
    return jsonify(pokemons_all, 200)


@bp.route("/get/<string:pokemon_id>", methods=["GET"])
def get_pokemon(pokemon_id):
    pokemon= pokemons.find_by_id(ObjectId(pokemon_id))
    return jsonify(pokemon, 200)

