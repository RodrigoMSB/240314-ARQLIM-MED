from TrabajadorDocumentosInterface import TrabajadorDocumentosInterface

class EmpleadoNormal(TrabajadorDocumentosInterface):
    """
    Clase que representa a un empleado normal.
    """

    def trabajar_documentos(self):
        """
        Método para trabajar con documentos.
        """
        print("Trabajando con documentos como empleado normal.")
