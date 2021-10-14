from Producto import Producto

class Orden:
    contador_orden = 0
    
    def __init__(self, productos):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)

    def agregar_produtos(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio

        return total

    def __str__(self):
        producto_str = ''
        for producto in self._productos:
            producto_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, \n {producto_str}'

if __name__ == '__main__':

    producto1 = Producto('Jabon', 2500)
    producto2 = Producto('Yerba', 5000)
    producto3 = Producto('Crema Dental', 7000)

    orden1 = Orden([producto1, producto2, producto3])

    print(orden1)
