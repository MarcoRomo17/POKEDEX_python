from app import mongo
from app.models.super_clase import SuperClass

class Pokemon(SuperClass): #el parentesis es para heredar
    def __init__(self):
        super().__init__("pokemons")#llama a la clase padre, lo iniciamos y ese wey ya espera la collecion

    def create(self, data):
        raise NotImplementedError("Los pokemones no se pueden crear")
       

    def delete(self, object_id):
        raise NotImplementedError("Los pokemones no se pueden eliminar")
      
    def update(self, object_id, data):
         raise NotImplementedError("Los pokemones no se pueden actualizar")
       
       

  

