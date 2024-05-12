from abc import ABC, abstractmethod

class AdministrativoInterface(ABC):
    """
    Interfaz para la funcionalidad administrativa.
    """

    @abstractmethod
    def realizar_tareas_administrativas(self):
        """
        Método abstracto para realizar tareas administrativas.
        """
        pass
