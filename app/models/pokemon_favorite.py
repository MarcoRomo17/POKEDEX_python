from app import mongo
from app.models.super_clase import SuperClass

class PokemonFavorites(SuperClass):
    def __init__(self, ):
        super().__init__("pokemon_favorites")#aqui va el nombre d ela colleccion

    def create(self, data):
        super().create(self, data)
       

    def delete(self, object_id):
        super().delete(self, object_id)
      
    def update(self, object_id, data):
        super().update(self, object_id, data)

    def find_all(self):
        super().find_all()

        
    def find_by_id(self, object_id):
        raise NotImplementedError("No es necesario traer todos los usuarios")

    
   