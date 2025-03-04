from app import mongo
from bson import ObjectId
from app.models.super_clase import SuperClass
#SE ESPECIFICA QUE NOOOOO SE VA A USAR
class PokemonFavorites(SuperClass):
    def __init__(self, ):
        super().__init__("pokemon_favorites")#aqui va el nombre d ela colleccion

    def update(self, object_id, data):
        raise NotImplementedError("No es necesario traer todos los usuarios")

    def find_all(self, user_id):#Modificamos el metodo para que filtre ates
        data=self.collection.find({"user_id": ObjectId(user_id)})
        for datum in data:
            datum["user_id"]=str(datum['user_id'])
            datum["pokemon_id"]=str(datum['pokemon_id'])
            datum["_id"]=str(datum['_id'])


        return data

        
    def find_by_id(self, object_id):
        raise NotImplementedError("No es necesario traer todos los usuarios")

    def create(self, data):
        data["user_id"]=ObjectId(data["user_id"])
        data["pokemon_id"]=ObjectId(data["pokemon_id"])
        datum = self.collection.insert_one(data)
        return str(datum.inserted_id)
