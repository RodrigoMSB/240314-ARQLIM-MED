from EmpleadoInterface import EmpleadoInterface

class EmpleadoNormal(EmpleadoInterface):
    """
    Clase que representa a un empleado normal.
    """

    def calcular_salario(self) -> float:
        """
        Calcula el salario del empleado normal.

        Returns:
            float: El salario calculado.
        """
        # Supongamos que el salario base es el único componente del salario
        return self.salario_base
