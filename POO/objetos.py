class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print('Hola mi nombre es: ', self.nombre, self.apellido)

usuario = Usuario('Felipe', 'Feliz')

usuario.saludo()
usuario.nombre = 'Chanchito'
usuario.saludo()

#eliminamos la propiedad nombre
del usuario.nombre

#eliminamos la instancia de la clase
del usuario
print(usuario)
