#las tuplas no pueden ser modificadas
tupla = (1, 2, 3, 4)

print(tupla)

#nos dice cuantas veces se repite
print(tupla.count(2))

#nos dice en que posicion esta el elemento que le pasamos entre los parentesis
print(tupla.index(1))

#convertimos una tupla a una lista
listaDeTupla = list(tupla)
print(listaDeTupla)

#cantidad de rango
rango = range(6)
print(rango)
