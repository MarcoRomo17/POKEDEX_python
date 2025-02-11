from app import mongo

class Users:
    collection = mongo.db.users

    #creamos metodos estaticos (no modificables)
    #Decorador
    @staticmethod
    def find_all():
        users = Users.collection.find()
        #lo anterior, devuelve un tipo cursor. No un arreglo. El cursor es un manejador de objetos
        #Entonces hay que cambiarlo a lista

        return list(users) #los hace lista
    
    @staticmethod
    def find_by_id(user_id):
        user=Users.collection.find_one({
            "_id":user_id
        })#las llaves son para hacer el filtro UWU
        return user #regresamos a un solo cabron
    
    @staticmethod
    def create(data):
        user= Users.collection.insert_one(data)
        return user.inserted_id
    
    @staticmethod
    def update(user_id, data):
        user = Users.collection.update_one({
            "_id":user_id
        },{
            "$set":data
        })#Filtro e info actualizar
        return user
    
    @staticmethod
    def delete(user_id):
        return Users.collection.delete_one({"_id":user_id})


    
    