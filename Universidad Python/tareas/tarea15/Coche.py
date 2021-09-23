from Vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, rueda, velocidad):
        super().__init__(color, rueda)
        self._velocidad = velocidad

    def __str__(self):
        return f'{super().__str__(self)} y va a una velocidad de {self._velocidad} k/m'

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad


