# Cuadrado.py
from Figura import Figura  # Importamos la clase Figura desde Figura.py

class Cuadrado(Figura):  # Heredamos de la clase Figura

    def __init__(self, lado):  # Corrección: es __init__ con doble guion bajo en cada lado
        self.lado = lado
        
    def area(self):
        return self.lado ** 2
        
    def perimetro(self):
        return self.lado * 4
