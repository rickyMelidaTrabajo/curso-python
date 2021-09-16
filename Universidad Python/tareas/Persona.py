class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def mostrarDetalles(self):
        print(f'Perona: {self._nombre} {self._apellido} {self._edad}')

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad



persona1 = Persona('Ricardo', 'Melida', 28)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


persona1.nombre = 'Anahi'
persona1.apellido = 'Encina'
persona1.edad = 25


print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


