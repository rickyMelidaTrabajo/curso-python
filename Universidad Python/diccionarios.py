data = {
        'nombre': 'Ricardo',
        'apellido': 'Melida',
        'edad': 29
}

for key, value in data.items():
    print(key, end=' ')
    print(f': {value}')


for key in data.keys():
    print(key)


for value in data.values():
    print(value)


#comprobar existencia de algun elemento
print('nombre' in data)
