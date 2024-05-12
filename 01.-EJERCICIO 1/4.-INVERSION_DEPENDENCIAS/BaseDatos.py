class BaseDatos:
    def guardar(self, datos):
        raise NotImplementedError()

    def leer(self):
        raise NotImplementedError()
