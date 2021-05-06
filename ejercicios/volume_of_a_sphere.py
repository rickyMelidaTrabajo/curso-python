# Escribir una funcion que devuelva el volumen de una esfera por su radio 4/3 * pi * r ** 3

def calcularVolumen(r):
    # En python la doble multiplicacion equivale a la potencia
    return 4 / 3 * 3.14 * r ** 3

resultado = calcularVolumen(6)
print(resultado)
