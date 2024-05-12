from abc import ABC, abstractmethod

class EmpleadoInterface(ABC):
    """
    Interfaz para los diferentes tipos de empleados.
    """

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def trabajar_documentos(self):
        """
        Método abstracto para trabajar con documentos.
        """
        pass

    @abstractmethod
    def asistir_reuniones(self):
        """
        Método abstracto para asistir a reuniones.
        """
        pass
