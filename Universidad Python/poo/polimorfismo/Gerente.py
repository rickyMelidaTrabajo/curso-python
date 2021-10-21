from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f'Gerente [Departamento: {self.department}] {super().__str__()}'
