from EmpleadoInterface import EmpleadoInterface

class EmpleadoNormal(EmpleadoInterface):
    """
    Clase que representa a un empleado normal.
    """

    def trabajar_documentos(self):
        """
        Método para trabajar con documentos.
        """
        print("Trabajando con documentos como empleado normal.")

    def asistir_reuniones(self):
        """
        Método para asistir a reuniones.
        """
        pass  # Los empleados normales no asisten a reuniones
