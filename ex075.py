from dataclasses import replace
from itertools import count
cont = cont01 = 0
num = (int(input('Digite um valor:')),
int(input('Digite outro valor:')),
int(input('Digite mais um valor:')),
int(input('Digite o último valor:')))
print('Os números digitados foram:',end=' ')
while True:
    print(num[cont],end=' ')
    cont+=1
    if cont == 4:
        break
print(f'\nO nove apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}° posição')
else:   
    print('O número 3 não apareceu')  
print('Os números pares são:',end='')
while True:
    if num[cont01] % 2 == 0:
        print(f'{num[cont01]}',end=' ')
    cont01 +=1
    if cont01 == 4:
        break    
