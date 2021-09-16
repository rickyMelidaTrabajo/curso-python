import os


try:
    os.remove('imagen')
    cont = os.listdir('./archivos')

    print(cont)
except:
    print('No se pudo leer el directorio')
