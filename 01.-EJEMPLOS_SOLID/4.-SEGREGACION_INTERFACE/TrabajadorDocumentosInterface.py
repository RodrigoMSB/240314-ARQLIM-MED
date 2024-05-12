from abc import ABC, abstractmethod

class TrabajadorDocumentosInterface(ABC):
    """
    Interfaz para la funcionalidad de trabajar con documentos.
    """

    @abstractmethod
    def trabajar_documentos(self):
        """
        Método abstracto para trabajar con documentos.
        """
        pass

