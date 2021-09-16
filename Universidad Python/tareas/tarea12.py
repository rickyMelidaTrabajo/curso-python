# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas. 
# Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe 
# imprimir: 5 4 3 2 1 Si se pasa el valor de 3, debe imprimir: 3 2 1 Si se 
# pasan valores negativos no imprime nada

def showValues(number):
    if number == 1:
        return 1
    else:
        print(number-1)
        return showValues(number-1)

showValues(5)
