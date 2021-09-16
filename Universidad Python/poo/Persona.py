class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Ricardo', 'Melida', 29)

print(f'Objeto persona1 : {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Anahi', 'Encina', 25)


print(f'Objeto persona2 : {persona2.nombre} {persona2.apellido} {persona2.edad}')
