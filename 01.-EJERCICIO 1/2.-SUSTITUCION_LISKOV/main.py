# main.py

# Importamos la clase Cuadrado desde el archivo Cuadrado.py
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# Creamos una instancia de la clase Cuadrado
cuadrado = Cuadrado(5)  # Crear un cuadrado con un lado de longitud 5

# Llamamos a los métodos area() y perimetro() de la instancia
area = cuadrado.area()
perimetro = cuadrado.perimetro()

# Imprimimos los resultados
print("Área Cuadrado:", area)
print("Perímetro Cuadrado:", perimetro)

# Creamos una instancia de la clase Rectangulo
rectangulo = Rectangulo(4, 6)  # Crear un rectángulo con base 4 y altura 6

# Llamamos a los métodos area() y perimetro() de la instancia
area = rectangulo.area()
perimetro = rectangulo.perimetro()

# Imprimimos los resultados
print("Área Rectángulo:", area)
print("Perímetro Rectángulo:", perimetro)