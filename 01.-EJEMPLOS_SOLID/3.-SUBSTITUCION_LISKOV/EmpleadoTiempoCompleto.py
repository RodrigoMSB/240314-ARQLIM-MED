from Empleado import Empleado

class EmpleadoTiempoCompleto(Empleado):
    """
    Clase que representa a un empleado a tiempo completo.
    """

    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        """
        Método para calcular el salario del empleado a tiempo completo.

        Returns:
            float: El salario del empleado.
        """
        # Suponemos que un mes tiene 160 horas laborables
        return self.salario_mensual / 160
