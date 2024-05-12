from abc import ABC, abstractmethod

class Empleado(ABC):
    """
    Clase abstracta para representar a un empleado.
    """

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario(self):
        """
        Método abstracto para calcular el salario del empleado.
        """
        pass
