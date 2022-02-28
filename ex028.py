from random import randint
from time import sleep

a = randint(0, 5)

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar')
print('-=-'*20)

num = int(input('Faça a sua aposta: '))

print('Processando...')

sleep(2)

if num == a:
    print(f'Você acertou!')

else:
    print(f'Você errou,eu pensei no {a} e você colocou {num} !')
