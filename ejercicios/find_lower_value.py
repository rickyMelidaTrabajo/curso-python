# Escribir una funcion que encuentre el elemento menor de una lista

lista = [1, 2, 3, 5, 55, -24, -12]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        #Quiero que menor sea igual a x siempre y cuanto x sea menor que menor,
        #Si no es asi no le cambies el valor que tenia
        menor = x if x < menor else menor

print('menor = ', menor)
