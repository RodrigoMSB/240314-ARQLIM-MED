from abc import ABC, abstractmethod

class Figura(ABC):
    """
    Clase abstracta para representar una figura geométrica.
    """
    
    @abstractmethod
    def area(self):
        """
        Método abstracto para calcular el área de la figura.
        """
        pass
        
    @abstractmethod
    def perimetro(self):
        """
        Método abstracto para calcular el perímetro de la figura.
        """
        pass
