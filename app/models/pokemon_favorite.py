from app import mongo
from bson import ObjectId
from app.models.super_clase import SuperClass
#SE ESPECIFICA QUE NOOOOO SE VA A USAR
class PokemonFavorites(SuperClass):
    def __init__(self, ):
        super().__init__("pokemon_favorites")#aqui va el nombre d ela colleccion

    def create(self, data):
        super().create(self, data)
       

    def delete(self, object_id):
        super().delete(self, object_id)
      
    def update(self, object_id, data):
        raise NotImplementedError("No es necesario traer todos los usuarios")

    def find_all(self, user_id):#Modificamos el metodo para que filtre ates
        data=self.collection.find({"user_id": ObjectId(user_id)})
        return data

        
    def find_by_id(self, object_id):
        raise NotImplementedError("No es necesario traer todos los usuarios")

    
   