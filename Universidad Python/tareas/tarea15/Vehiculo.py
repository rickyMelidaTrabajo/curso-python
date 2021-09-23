#Definir una clase padre llamada Vehiculo 
#y dos clases hijas llamadas Coche y Bicicleta, 
#las cuales heredan de la clase Padre Vehiculo

class Vehiculo:
    def __init__(self, color, rueda):
        self._color = color
        self._rueda = rueda

    def __str__(self):
        return f'El vehiculo es de color {color} y tiene {rueda} ruedas'

    @property
    def color(self):
        return self._color

    @property 
    def rueda(self):
        return self._rueda

    @color.setter
    def color(self, color):
        self._color = color

    @rueda.setter
    def rueda(self, rueda):
        self._rueda = rueda


