class MiClase:
    variable_clase = 'valor de variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()

MiClase.metodo_clase()
miObjeto = MiClase('Mi variable de instancia')
miObjeto.metodo_instancia()

