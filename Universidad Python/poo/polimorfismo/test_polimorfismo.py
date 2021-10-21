from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalle(objeto):
    #print(objeto)
    print(objeto.mostrar_detalle())

    if isinstance(objeto, Gerente):
        print(objeto)

    print(type(objeto))

empleado = Empleado('Ricardo', 5555)
imprimir_detalle(empleado)

gerente = Gerente('Juan', 6000, 'Sistemas')
#imprimir_detalle(gerente)
