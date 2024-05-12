from TrabajadorDocumentosInterface import TrabajadorDocumentosInterface
from AsistenteReunionesInterface import AsistenteReunionesInterface
from AdministrativoInterface import AdministrativoInterface

class EmpleadoAdministrativo(TrabajadorDocumentosInterface, AsistenteReunionesInterface, AdministrativoInterface):
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

    def realizar_tareas_administrativas(self):
        """
        Método para realizar tareas administrativas.
        """
        print("Realizando tareas administrativas.")
