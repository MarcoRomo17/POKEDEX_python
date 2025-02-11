from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from dotenv import load_dotenv
import os 

load_dotenv()#Para usar el .env

mongo = PyMongo()

#Configuracion inicial
def create_app():
    app= Flask(__name__)
    app.config["MONGO_URI"]= os.getenv("MONGO_URI")#obtiene la variable de ambiente y la pone en la posicion d emomgo uri
    mongo.init_app(app)

    CORS(app)
    return app

