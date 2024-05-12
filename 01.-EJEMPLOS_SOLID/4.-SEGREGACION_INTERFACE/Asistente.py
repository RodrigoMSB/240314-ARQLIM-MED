from TrabajadorDocumentosInterface import TrabajadorDocumentosInterface
from AsistenteReunionesInterface import AsistenteReunionesInterface

class Asistente(TrabajadorDocumentosInterface, AsistenteReunionesInterface):
    """
    Clase que representa a un asistente.
    """

    def trabajar_documentos(self):
        """
        Método para trabajar con documentos.
        """
        print("Trabajando con documentos como asistente.")

    def asistir_reuniones(self):
        """
        Método para asistir a reuniones.
        """
        print("Asistiendo a reuniones como asistente.")
