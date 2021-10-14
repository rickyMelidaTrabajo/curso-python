class Persona:
    contador_persona = 0
    
    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'[ {self.nombre} {self.edad }  {self.id_persona}]'


persona1 = Persona('Ricardo', 29)
print(persona1)
persona2 = Persona('Anahi', 25)
print(persona2)
