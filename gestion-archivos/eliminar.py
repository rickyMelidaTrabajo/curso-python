import os

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
    print('Archivo eliminado')
else:
    print('El archivo no existe')

#eliminamos una carpeta
os.rmdir('miCarpeta')
