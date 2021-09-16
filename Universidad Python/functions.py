def myFunction(*names):
    for name in names:
        print(name)

def sumaNum(*args):
    sum=0
    for arg in args:
        sum +=arg

    return sum

#Aqui recibe como parametro un diccionario
#el cual recorremos e imprimimos sus valores
def listarNumeros(**k):
    for llave, valor in k.items():
        print(f'{llave}: {valor}')



def factorialRecursiva(numero):
    if numero ==1:
        return 1
    else:
        return numero * factorialRecursiva(numero-1)

#listarNumeros(IDE='Integrated Development Envirement', pk="primary key")
#print(sumaNum(2,2,2,2,2))

#Aqui podemos agregar una cantida n de parametros
#y Python lo guarda como tupla
#myFunction('Anahi', 'Debora', 'Ricardo')

print(factorialRecursiva(5))

