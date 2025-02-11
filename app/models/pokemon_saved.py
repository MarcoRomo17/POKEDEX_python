from app import mongo

class Pokemon_saved:
    collection = mongo.db.pokemons_saved

    #creamos metodos estaticos (no modificables)
    #Decorador
    @staticmethod
    def find_all():
        pokemons = Pokemon_saved.collection.find()
        #lo anterior, devuelve un tipo cursor. No un arreglo. El cursor es un manejador de objetos
        #Entonces hay que cambiarlo a lista

        return list(pokemons) #los hace lista
    
    @staticmethod
    def find_by_id(pokemon_id):
        pokemon=Pokemon_saved.collection.find_one({
            "_id":pokemon_id
        })#las llaves son para hacer el filtro UWU
        return pokemon #regresamos a un solo cabron
    
    @staticmethod
    def create(data):
        pokemon= Pokemon_saved.collection.insert_one(data)
        return pokemon.inserted_id
    
    @staticmethod
    def update(pokemon_id, data):
        pokemon = Pokemon_saved.collection.update_one({
            "_id":pokemon_id
        },{
            "$set":data
        })#Filtro e info actualizar
        return pokemon
    
    @staticmethod
    def delete(pokemon_id):
        return Pokemon_saved.collection.delete_one({"_id":pokemon_id})


    
    