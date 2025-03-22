from app import mongo
from app.models.super_clase import SuperClass
class User(SuperClass):
    def __init__(self):
        super().__init__("users")#llama a la clase padre, lo iniciamos y ese wey ya espera la collecion



    def find_all(self):
        raise NotImplementedError("No es necesario traer todos los usuarios")
    

     
    def get_by_email_password(self, email):
        print(email, "soy el email recibido")
        user = self.collection.find_one({"email": email})
        if not user:
            return None
        user["_id"]=str(user["_id"])
        print("regresare ", user)
        return user
