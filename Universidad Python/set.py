planetas = { 'Marte', 'Jupiter', 'Venus' }

print(planetas)

print('Marte' in planetas)

#agregar un elemento
planetas.add('Tierra')

print(planetas)

#eliminar elemento sin arrojar error
planetas.discard('Tierras')
