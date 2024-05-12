from Animal import Animal
from abc import abstractmethod

class Carnivoro(Animal):

    @abstractmethod
    def cazar(self):
        pass
