from GestorEmpleadosInterface import GestorEmpleadosInterface
from EmpleadoInterface import EmpleadoInterface

class GestorEmpleados(GestorEmpleadosInterface):
    """
    Clase que gestiona empleados.
    """

    def __init__(self):
        self.empleados = []

    def contratar_empleado(self, empleado: EmpleadoInterface):
        """
        Contrata a un empleado.

        Args:
            empleado (EmpleadoInterface): El empleado a contratar.
        """
        self.empleados.append(empleado)
        print(f"Empleado {empleado.nombre} contratado.")

    def despedir_empleado(self, empleado: EmpleadoInterface):
        """
        Despide a un empleado.

        Args:
            empleado (EmpleadoInterface): El empleado a despedir.
        """
        self.empleados.remove(empleado)
        print(f"Empleado {empleado.nombre} despedido.")
