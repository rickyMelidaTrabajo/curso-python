def miFuncion():
    print('Mi primera funcion')

#miFuncion()

def imprimeDato(nombre, apellido):
    print('Mi argumento es: ', nombre, apellido)

#imprimeDato('Ricardo', 'Melida')

def imprimeTupla(*data):
    print(data[0])

#imprimeTupla('Chanchito', 'Feliz', 'lala', 'lele')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

#nombreCompleto(nombre='Ricardo', apellido='Melida')

def nombreCompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

#nombreCompleto2(nombre='Anahi', apellido='Encina')


def miFuncion2(nombre='Ricardo'):
    print(nombre)

#miFuncion2('Anahi')

def miFuncionLista(lista):
    for el in lista:
        print(el)

#miFuncionLista(['Ricardo', 'Melida'])


def concatenaNombre(lista):
    i=''
    for el in lista:
        i = i + el + ' '
    return i

nombres = concatenaNombre(['Nelly', 'Anahi', 'Ruiz Diaz'])

print(nombres)

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)
