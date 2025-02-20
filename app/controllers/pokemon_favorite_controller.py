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
from tools.response_manager import ResponseManager

bp = Blueprint("pokemon_favorite",__name__, url_prefix="/pokemon_favorite")#Carpeta u endpoint

RM= ResponseManager()
pok_fav_schema= Pokemon_Favorite_Schema()
pok_fav_model= ModelFactory.get_model("pokemon_favorites")

@bp.route("/", methods=["POST"])
def create():
    try:
        data=request.json

        data= pok_fav_schema.validate(data)
        pokFav_id=pok_fav_model.create(data) #Creamos el usuario, regres aun OBJ ID
        return RM.succes({"pokFav_id":pokFav_id}) #Mandamos respuesta json con el obj ide en texto

    except ValidationError as err:
        print(err)
        return RM.error("Los parametros enviados son incorrectos")
    

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
    return RM.succes("Pokemon eliminado con exito")



#MODIFICAR para que traiga por id
@bp.route("/get", methods=["GET"])
def get_ALL_POKES_FAV(user_id):
    pokem= pok_fav_model.find_all(user_id)

    return RM.succes(pokem) #regresamos el arreglo


#TRAER TODOS LOS POKEMONES Y UNO SOLO

