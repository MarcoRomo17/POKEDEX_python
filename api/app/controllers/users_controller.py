from flask import Blueprint, request #secciona el servidor en urls
#request maneja la peticion dle usuario
#Jsonify maneja las respuesta al usuario

from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.tools.encription_manager import EncryptionManager

RM= ResponseManager()
EM= EncryptionManager()
bp = Blueprint("users",__name__, url_prefix="/users")#Carpeta u endpoint
#dice que todo lo que tenga el prefihjo users va a venir aqui
user_schema= UserSchema()
user_model = ModelFactory.get_model("users") #mandamos a traer el modelo

@bp.route("/login", methods=["POST"])
def login():
    
    data = request.json
    email= data.get("email", None) #Pedimos un parametro, si no existe devuekve un None
    password= data.get("password", None)
    print(email, password, "hola desde el login")

    if not email or not password:
        return RM.error("Es necesario enviar todas las credenciales")
    print(email, password, "hola desde el login 2")

    user= user_model.get_by_email_password(email)
    print(user, "soy lo que me devolvio la llamada al back")
    if not user: 
        return RM.error({"msg":"No se encontro un usario", "regreso":user})
    
    if not EM.compare_hashes(password,user["password"]):
        return RM.error("Credenciales invalidas")
    return RM.succes({"user":user, "token":create_access_token(str(user["_id"]))})

#REGISTRAR USUARIO
@bp.route("/register", methods=["POST"])
def register():
    
    try:
        data = user_schema.load(request.json)#Mandamos a evaluar los dtos
        print(data)
        data["password"]=EM.create_hash(data["password"])
        print(data)
        user_id=user_model.create(data) #Creamos el usuario, regres aun OBJ ID
        return RM.succes({"user_id":str(user_id),"token":create_access_token(str(user_id))}) #Mandamos respuesta json con el obj ide en texto
    except ValidationError as err:
        return RM.error(str(err))
        
    

#endpoint para actualizar. Mandamos un id por la ruta
@bp.route("/update", methods=["PUT"]) #ahuevo requiere todos los parametros
@jwt_required()
def update():
    user_id=get_jwt_identity()
    print(user_id)
    try:
        data= user_schema.load(request.json)
        data["password"]=EM.create_hash(data["password"])
        user= user_model.update(ObjectId(user_id), data)
        return RM.succes({
            "data": user
        })


    except ValidationError as err:
        return RM.error("Los parametros enviados son incorrectos")
    
@bp.route("/delete", methods=["DELETE"])
@jwt_required()
def delete():
    user_id=get_jwt_identity()
    user_model.delete(ObjectId(user_id))
    return RM.succes("Usuario eliminado con exito")


@bp.route("/get", methods=["GET"])
@jwt_required()
def get_user():
    user_id=get_jwt_identity()
    user= user_model.find_by_id(ObjectId(user_id))
    if not user:
        return RM.error("El usaurio no existe")
    return RM.succes(user)