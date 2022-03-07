número = int(input('Digite um número inteiro:'))

contador = 0

for c in range(1, número + 1):
    if número % c == 0:
        contador += 1

print(f'O número {número} foi divisível em {contador} situações')

if contador == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')  