usuarios = ['chanchito feliz', 'felipe', 'roberto', 'nicolas']

#for usuario in usuarios:
#    if usuario == 'roberto':
#        break
#    print(usuario)

nombre = 'Ricardo'

#for c in nombre:
#    if c == 'a':
#        continue;
#    print(c)

#el primer valor es en cuanto va a empezar
#el segundo valor hasta cuando va a contar
#el tercer valor indica cada cuanto va a contar
for x in range(3, 30, 3):
    print(x)
#en los loop cuando se agrega un else, este se ejecuta una vez que
#finalice toda la iteracion
else:
    print('Hemos terminado')

edades = [24, 25, 26, 35]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)
