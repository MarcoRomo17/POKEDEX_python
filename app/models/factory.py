from app.models.pokemon import Pokemon
from app.models.users import User
from app.models.pokemon_favorite import PokemonFavorites

class ModelFactory:
    @staticmethod
    def get_model(collection_name):
        models ={
            "users": User,
            "pokemons": Pokemon,
            "pokemon_favorites": PokemonFavorites
        }
        if collection_name in models:
            return models[collection_name]()#regresamos la instancia y la podemos usar en los controladores
        raise ValueError(f"El modelo enviada: {collection_name} no existe")