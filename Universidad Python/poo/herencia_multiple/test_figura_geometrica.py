from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creacion Objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado=5, color='Rojo')
cuadrado1.alto = -10
print(cuadrado1.calcularArea())
print(cuadrado1)


print('Crecion Objeto Rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(3, -9, 'Green')
print(rectangulo1.calcularArea())
print(rectangulo1)
