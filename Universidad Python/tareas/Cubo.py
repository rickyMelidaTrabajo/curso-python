class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def calculaVolumen(self):
        return self.ancho * self.alto * self.profundo



ancho = int(input('Proporciona al ancho: '))
alto = int(input('Proporciona el alto: '))
profundo = int(input('Proporciona lo profundo: '))

miCubo = Cubo(ancho, alto, profundo)

print(f'Volumen cubo: {miCubo.calculaVolumen()}')
