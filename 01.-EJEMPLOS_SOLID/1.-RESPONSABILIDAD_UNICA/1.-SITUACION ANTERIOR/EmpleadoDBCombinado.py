class EmpleadoDBCombinado:
    
    def __init__(self, id_empleado, nombre, puesto):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.puesto = puesto

    def get_info_empleado(self):
        return f"ID: {self.id_empleado}, Nombre: {self.nombre}, Puesto: {self.puesto}"

    def guardar_empleado(self):
        # Aquí iría la lógica para guardar el empleado en la base de datos
        # Nota: Usaríamos los atributos de esta misma instancia para guardar la información
        pass

    def eliminar_empleado(self):
        # Aquí iría la lógica para eliminar este empleado de la base de datos
        # Nota: Podríamos usar el ID del empleado de esta instancia para eliminarlo
        pass

    # Más métodos relacionados tanto con la gestión del empleado como con la base de datos...
