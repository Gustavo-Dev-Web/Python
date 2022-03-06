num = int(input('Digite um número inteiro:'))
total = 0
for c in range(1, num+1):
    if num % c == 0:
        print(end='')
        total += 1
    else:
        print(end='')
print(f'O número {num} foi divisível em {total} situações')
if total == 2:
    print('Por isso ele é PRIMO')
else:
    print('Por isso ele NÃO É PRIMO')           