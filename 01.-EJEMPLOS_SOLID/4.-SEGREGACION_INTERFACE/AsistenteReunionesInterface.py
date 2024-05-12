from abc import ABC, abstractmethod

class AsistenteReunionesInterface(ABC):
    """
    Interfaz para la funcionalidad de asistir a reuniones.
    """

    @abstractmethod
    def asistir_reuniones(self):
        """
        Método abstracto para asistir a reuniones.
        """
        pass

