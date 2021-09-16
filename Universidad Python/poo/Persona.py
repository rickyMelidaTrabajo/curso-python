class Persona:
    #con *args podemos recibir tuplas y **kwargs para recibir un diccionario de datos
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self):
        print(f'Objeto Persona: {self.nombre} {self.apellido} {self.edad} {self.args} {self.kwargs}')

persona1 = Persona('Ricardo', 'Melida', 29, '0991470681', 2, 3, 5, m='manzana', p='pera')



persona1.mostrarDetalle()


persona2 = Persona('Anahi', 'Encina', 25)


persona2.mostrarDetalle()


