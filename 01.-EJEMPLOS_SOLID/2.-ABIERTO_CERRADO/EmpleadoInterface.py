from abc import ABC, abstractmethod

class EmpleadoInterface(ABC):
    """
    Interfaz para los diferentes tipos de empleados.
    """

    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self) -> float:
        """
        Método abstracto para calcular el salario del empleado.
        """
        pass
