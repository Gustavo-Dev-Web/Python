a = float(input('Aqui vai o número 1: '))
b = float(input('Aqui vai o número 2: '))
c = float(input('Aqui vai o número 3: '))

maior = a
if  b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f'O menor é: {menor :.0f}')
print(f'O maior é: {maior :.0f}')
