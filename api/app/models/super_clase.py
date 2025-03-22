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
            #for datum in list(data):
                #datum["_id"]=str(datum["_id"])
        return list(data) #los hace lista
    
   
    def find_by_id(self,object_id):
        datum=self.collection.find_one({
            "_id":object_id
        })#las llaves son para hacer el filtro UWU
        if datum:
            datum["_id"]=str(datum["_id"])
        return datum #regresamos a un solo cabron
    
   
    def create(self,data):
        print(data)
        datum= self.collection.insert_one(data)
        return str(datum.inserted_id)
    
   
    def update(self,object_id, data):
        self.collection.update_one({
            "_id":object_id
        },{
            "$set":data
        })#Filtro e info actualizar
        datum = self.collection.find_one({
            "_id":object_id
        })
        datum["_id"]=str(datum['_id'])
        return datum
    
   
    def delete(self,object_id):
        return self.collection.delete_one({"_id":object_id})


    
    