class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    def __str__(self):
        return f'Persona: [Nombre: {self.nombre}, Edad: {self.edad}]'

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @edad.setter
    def edad(self, edad):
        self._edad = edad


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property 
    def sueldo(self):
        return self._sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'


empleado1 = Empleado('Juan', 30, 2000)
print(empleado1.edad)
