from adaptador import Adaptador
from usuario import Usuario

class RepositorioUsuario:
    def __init__(self):
        self.adaptador = Adaptador()

    def crear(self, nombre, correo, contraseña):
        query = "INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)"
        parametros = (nombre, correo, contraseña)
        try:
            self.adaptador.ejecutar_query(query, parametros)
            return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False
