from random import randint
from time import sleep
lista = []
lista02 = []
print(f'{"VAMOS SORTEAR NÚMEROS NA MEGA SENA"}')
jogos = int(input(f'Você quer fazer quantos jogos? '))
print('-='*35)
for c in range(1,jogos+1):
    while len(lista02) < 6:
        num = randint(1,60)
        if num not in lista02:
            lista02.append(num)
    lista02.sort()
    lista.append(lista02[:])
    lista02.clear()
    print(f'Jogo {c}: {lista[c-1]} ')
    sleep(0.7)
print('-='*35)
