from EmpleadoInterface import EmpleadoInterface

class CalculadoraSalario:
    """
    Clase responsable de calcular el salario de un empleado.
    """

    def calcular_salario(self, empleado: EmpleadoInterface) -> float:
        """
        Calcula el salario del empleado dado.

        Args:
            empleado (EmpleadoInterface): El empleado para el cual se calculará el salario.

        Returns:
            float: El salario calculado.
        """
        return empleado.calcular_salario()
