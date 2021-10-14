from Producto import Producto
from Orden import Orden

producto1 = Producto('Reloj', 500.0)
producto2 = Producto('Yerba', 50.0)
producto3 = Producto('Kitadol', 20.0)

orden1 = Orden([producto1, producto2, producto3])

print(f'Total: {orden1.calcular_total()}')
