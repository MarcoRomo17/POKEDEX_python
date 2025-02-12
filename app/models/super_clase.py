from app import mongo

class SuperClass:

    def __init__(self, collection):
        self.collection= mongo.db[collection] #hacemos la coleccion dinamica


    #creamos metodos estaticos (no modificables)
    #Decorador
   
    def find_all(self):
        data = self.collection.find()
        #lo anterior, devuelve un tipo cursor. No un arreglo. El cursor es un manejador de objetos
        #Entonces hay que cambiarlo a lista

        return list(data) #los hace lista
    
   
    def find_by_id(self,object_id):
        datum=self.collection.find_one({
            "_id":object_id
        })#las llaves son para hacer el filtro UWU
        return datum #regresamos a un solo cabron
    
   
    def create(self,data):
        datum= self.collection.insert_one(data)
        return datum.inserted_id
    
   
    def update(self,object_id, data):
        datum = self.collection.update_one({
            "_id":object_id
        },{
            "$set":data
        })#Filtro e info actualizar
        return datum
    
   
    def delete(self,object_id):
        return self.collection.delete_one({"_id":object_id})


    
    