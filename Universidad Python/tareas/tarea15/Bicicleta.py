from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, rueda, tipo):
        super().__init__(color, rueda)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} y es de tipo {self._tipo}'

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo
