from math import hypot
a = float(input('Cateto Oposto:'))
b = float(input('Cateto Adjacente:'))

result = hypot(a,b)

print(f'Hipotenusa é igual a: {result:.2f}')
