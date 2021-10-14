# Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho): 
        if self._validar_valor(ancho):
            self._ancho = ancho 
        else:
            self._ancho = 0
            print(f'Valor erroneo {ancho}')

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo {alto}')
    
    def __str__(self):
        return f'El ancho es: {self._ancho} y el alto: {self._alto}'

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if _validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo alto: {alto}')

    @property
    def ancho(self):
        
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if _valida_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @abstractmethod
    def calcular_area(self):
        pass

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False
    
