from BaseDatos import BaseDatos
from pymongo import MongoClient

class MongoDB(BaseDatos):
    def guardar(self, datos):
        # Implementación para guardar en MongoDB
        # Aquí se conectaría a la base de datos MongoDB y se guardarían los datos
        print("Guardando datos en MongoDB:", datos)

    def leer(self):
        # Implementación para leer de MongoDB
        # Aquí se conectaría a la base de datos MongoDB y se leerían los datos
        return "Datos leídos de MongoDB"
