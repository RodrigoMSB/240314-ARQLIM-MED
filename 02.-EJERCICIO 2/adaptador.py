import mysql.connector

class Adaptador:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ARQ'
        )

    def ejecutar_query(self, query, parametros=None):
        cursor = self.conexion.cursor()
        if parametros:
            cursor.execute(query, parametros)
        else:
            cursor.execute(query)
        self.conexion.commit()
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
