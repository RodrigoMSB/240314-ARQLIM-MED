from abc import ABC, abstractmethod
from EmpleadoInterface import EmpleadoInterface

class GestorEmpleadosInterface(ABC):
    """
    Interfaz para gestionar empleados.
    """

    @abstractmethod
    def contratar_empleado(self, empleado: EmpleadoInterface):
        """
        Contrata a un empleado.

        Args:
            empleado (EmpleadoInterface): El empleado a contratar.
        """
        pass

    @abstractmethod
    def despedir_empleado(self, empleado: EmpleadoInterface):
        """
        Despide a un empleado.

        Args:
            empleado (EmpleadoInterface): El empleado a despedir.
        """
        pass
