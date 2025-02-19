#Solo se crea actualiza elimina y trae todos
#Modificar la clase del modelo y evitar que se usen metodos indebidos

#pokemon id y user id

from flask import Blueprint, request, jsonify #secciona el servidor en urls
#request maneja la peticion dle usuario
#Jsonify maneja las respuesta al usuario

from app.schemas.pokemon_favorites_shcemas import Pokemon_Favorite_Schema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemon_favorite",__name__, url_prefix="/pokemon_favorite")#Carpeta u endpoint

pok_fav_schema= Pokemon_Favorite_Schema()
pok_fav_model= ModelFactory.get_model("pokemon_favorites")

@bp.route("/register", methods=["POST"])
def register():
    try:
        data = pok_fav_schema.load(request.json)#Mandamos a evaluar los dtos
        pokFav_id=pok_fav_model.create(data) #Creamos el usuario, regres aun OBJ ID
        return jsonify({"pokFav_id":str(pokFav_id)},200) #Mandamos respuesta json con el obj ide en texto

    except ValidationError as err:
        return jsonify("Los parametros enviados son incorrectos", 400)
    

#endpoint para actualizar. Mandamos un id por la ruta
@bp.route("/update/<string:pokFav_id>", methods=["PUT"])
def update(pokFav_id, ):
    try:
        data= pok_fav_schema.load(request.json)
        pok_fav= pok_fav_model.update(ObjectId(pokFav_id), data)
        return jsonify({
            "data": pok_fav
        }, 200)


    except ValidationError as err:
        return jsonify("Los parametros enviados son incorrectos", 400)
    
@bp.route("/delete/<string:pokFav_id>", methods=["DELETE"])
def delete(pokFav_id):
    pok_fav_model.delete(ObjectId(pokFav_id))
    return jsonify("Usuario eliminado con exito", 200)



#MODIFICAR para que traiga por id
@bp.route("/get", methods=["GET"])
def get_ALL_POKES_FAV(user_id):
    pokem= pok_fav_model.find_all()
    pokemons_filtered=[]

    for pokemon in pokem:
        if pokemon.user_id ==user_id:
            pokemons_filtered.append(pokemon)
    return jsonify(pokemons_filtered, 200)


#TRAER TODOS LOS POKEMONES Y UNO SOLO

