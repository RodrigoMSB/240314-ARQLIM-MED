class Empleado:
    
    def __init__(self, id_empleado, nombre, puesto):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto

    def get_info_empleado(self):
        return f"ID: {self.id_empleado}, Nombre: {self.nombre}, Puesto: {self.puesto}"
