from BaseDatos import BaseDatos
import mysql.connector

class MySQL(BaseDatos):
    def guardar(self, datos):
        # Implementación para guardar en MySQL
        # Aquí se conectaría a la base de datos MySQL y se guardarían los datos
        print("Guardando datos en MySQL:", datos)

    def leer(self):
        # Implementación para leer de MySQL
        # Aquí se conectaría a la base de datos MySQL y se leerían los datos
        return "Datos leídos de MySQL"
