from modulos import saludo, mascotas
from camelcase import CamelCase

print(mascotas)
saludo('Ricardo')

c = CamelCase()
s = 'esta oracion necesita CamelCase'

print(c.hump(s))
