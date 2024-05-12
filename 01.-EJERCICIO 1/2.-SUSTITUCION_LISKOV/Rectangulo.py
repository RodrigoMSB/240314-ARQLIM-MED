# Rectangulo.py

from Figura import Figura  # Importamos la clase Figura desde Figura.py

class Rectangulo(Figura):  # Heredamos de la clase Figura

    def __init__(self, base, altura):  # Corrección: es __init__ con doble guion bajo en cada lado
        """
        Constructor de la clase Rectangulo.
        
        Args:
            base (float): La longitud de la base del rectángulo.
            altura (float): La altura del rectángulo.
        """
        self.base = base
        self.altura = altura
        
    def area(self):
        """
        Método para calcular el área del rectángulo.
        
        Returns:
            float: El área del rectángulo.
        """
        return self.base * self.altura
        
    def perimetro(self):
        """
        Método para calcular el perímetro del rectángulo.
        
        Returns:
            float: El perímetro del rectángulo.
        """
        return (2 * self.base) + (2 * self.altura)
