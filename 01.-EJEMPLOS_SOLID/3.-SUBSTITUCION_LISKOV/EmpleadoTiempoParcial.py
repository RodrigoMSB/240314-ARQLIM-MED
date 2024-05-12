from Empleado import Empleado

class EmpleadoTiempoParcial(Empleado):
    """
    Clase que representa a un empleado a tiempo parcial.
    """

    def __init__(self, nombre, horas_trabajadas, salario_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.salario_hora = salario_hora

    def calcular_salario(self):
        """
        Método para calcular el salario del empleado a tiempo parcial.

        Returns:
            float: El salario del empleado.
        """
        return self.horas_trabajadas * self.salario_hora
