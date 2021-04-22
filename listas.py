lista = [1,2,3]
print(lista)
#con copy() copiamos todo lo que haya en la variable lista
lista2 = lista.copy()
lista2.append(4)
print(lista2)
#lista.clear()
print(lista)

#count(x)  nos dice cuanta veces se repite x numero
print(lista2.count(2))

#con len(x) nos dice la longitud que tiene la lista
print('La lista tiene ' + str(len(lista)) + ' elementos')

#accedemos al primer elemento de la lista
#print(lista[0])

#eliminamos el ultimo elemento de la lista
lista.pop()
print(lista)

#con esto eliminamos el elemento seleccionado entre los parentesis
#lista2.remove(2)
#print(lista2)

#con reverse invertimos el orden de la lista
lista2.reverse()
print(lista2)

#con sort ordenamos una lista
#para poder ordenar una lista, estas deben de ser de un mismo tipo de dato
lista2.sort()
print(lista2)

