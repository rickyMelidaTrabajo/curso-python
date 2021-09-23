class Persona:
    #con *args podemos recibir tuplas y **kwargs para recibir un diccionario de datos
    #def __init__(self, nombre, apellido, edad, *args, **kwargs):
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        #self.args = args
        #self.kwargs = kwargs

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self_edad

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @edad.setter
    def edad(self, edad):
        self._edad = edad   


    def mostrarDetalle(self):
        #print(f'Objeto Persona: {self._nombre} {self._apellido} {self._edad} {self.args} {self.kwargs}')
        print(f'Objeto Persona: {self._nombre} {self._apellido} {self._edad}')


    #Metodo destructor de la clase Persona
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona('Ricardo', 'Melida', 29)

    persona1.mostrarDetalle()

    persona1.nombre = 'Anahi'


    persona1.mostrarDetalle()
