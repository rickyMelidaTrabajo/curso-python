#Permisos para acceder a los archivos:
#r (read)   leer el archivo
#a (append) agregar al final del archivos mas texto
#w (write)  si el archivo no existe, python lo crea, si existe lo modifica completamente
#x con esto creamos un archivo sino existe, y si existe nos va a dar un error
c = open('chanchito.txt')

#Leemos la totalidad del texto
#print(c.read())

#Leemos una por una las lineas
#print(c.readline())
#print(c.readline())
#print(c.readline())

for x in c:
    #x es cada una de las lineas que estamos leyendo
    print(x)

#Una vez que hayamos leido todo el archivo debemos de cerrarlo
c.close()
