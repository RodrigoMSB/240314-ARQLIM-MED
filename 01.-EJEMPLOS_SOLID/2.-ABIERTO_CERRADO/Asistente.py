from EmpleadoInterface import EmpleadoInterface

class Asistente(EmpleadoInterface):
    """
    Clase que representa a un asistente.
    """

    def calcular_salario(self) -> float:
        """
        Calcula el salario del asistente.

        Returns:
            float: El salario calculado.
        """
        # Supongamos que el salario base es el único componente del salario
        return self.salario_base
