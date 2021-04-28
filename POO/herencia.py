class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print('Hola mi nombre es: ', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola me llamo: ', self.nombre, ' y soy el administrador')

admin = Admin('Super', 'Feliz')
admin.saludo()
admin.superSaludo()
