from random import randint

contador = 0
a = 0
numero = 1

while numero != a:
    a = randint(1,10)
    numero = int(input('Escolha um número:'))
    if numero != a:
        contador += 1
    elif numero == a:
        print(f'Parabéns após {contador+1} chances nós dois pensamos no número {a}')   
