diccionario = { 
    "nombre": "Jordan",
    "raza" : "Pez",
    "edad": 5
}

#print(diccionario)

#print(diccionario['nombre'])

#con el metodo get tambien se puede obtener el valor de un elemento
#print(diccionario.get('edad'))

#con esto modificamos el valor de un elemento especifico
diccionario['raza'] = 'Persa'
#print(diccionario)

#print(len(diccionario))

#Agregamos un nuevo elemento al diccionario
diccionario['ronronea'] = 'Si'
#print(diccionario)

#eliminamos un elemento seleccionado
#diccionario.pop('ronronea')

#popitem elimina el ultimo elemento de un diccionario
#diccionario.popitem()


#tambien podemos eliminar un elemento de un diccionario con del
#del diccionario['ronronea']
#print(diccionario)

#Podemos hacer una copia de nuestro diccionario con copy
#copiaGatito = diccionario.copy()

#tambien podemos copiar un diccionario con dict
copiaGatito = dict(diccionario)
#print(copiaGatito)

#podemos vaciar un diccionario con clear
#diccionario.clear()

fluffy = {
    "nombre": "Fluffy",
    "edad" : 4
}

mamba = {
    "nombre": "Mamba",
    "edad" : 12
}

gatitos = {
    "Fluffy" : fluffy,
    "Mamba": mamba
}

print(gatitos)

#Podemos crear un nuevo diccionario con constructor dict
perritos = dict(nombre="Chanchito Feliz", edad=6)
print(perritos)

verdadero = True
falso  = False
