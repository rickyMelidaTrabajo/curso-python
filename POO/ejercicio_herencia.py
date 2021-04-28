class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola soy un',  self.tipo, ' y mi sonido es el: ', self.onomatopeya)
        

class Gato(Animal):
    tipo = 'gato'
    
    #Extendemos el metodo init de la clase padre
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola soy un gato extendido')

class Perro(Animal): 
    tipo = 'perro'
    #Extendemos el metodo init de la clase padre
    def __init__(self, nombre, onomatopeya):
        #Aqui no hace falta agregar la palabra reservada self
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()
