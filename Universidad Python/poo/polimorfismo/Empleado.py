class Empleado:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Empleado : [Nombre: {self.name} Salario: {self.salary}]'

    def mostrar_detalle(self):
        return self.__str__();
