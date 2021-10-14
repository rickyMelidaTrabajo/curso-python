from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creacion Objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='Rojo')
cuadrado1.lado = 10
print(cuadrado1.calcular_area())
print(cuadrado1)


print('Crecion Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, -9, 'Green')
print(rectangulo1.calcular_area())
print(rectangulo1)
