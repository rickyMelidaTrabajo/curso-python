# Escribir una funcion que reciba nombre y apellido y los vaya agregando a
# un archivo

def agregaNombreAArchivo(nombre, apellido):
    c = open('nombrecompleto.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()


nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')

agregaNombreAArchivo(nombre, apellido)
