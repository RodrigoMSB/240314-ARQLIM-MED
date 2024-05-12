from EmpleadoInterface import EmpleadoInterface

class EmpleadoAdministrativo(EmpleadoInterface):
    """
    Clase que representa a un empleado administrativo.
    """

    def trabajar_documentos(self):
        """
        Método para trabajar con documentos.
        """
        print("Trabajando con documentos como empleado administrativo.")

    def asistir_reuniones(self):
        """
        Método para asistir a reuniones.
        """
        print("Asistiendo a reuniones como empleado administrativo.")
