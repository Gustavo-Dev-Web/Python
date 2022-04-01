from random import randint
from time import sleep
lista = []
dicionário = {}
cont = 0
for c in range(0,4):
    dicionário["jogador"] = randint(1,6)
    lista.append(dicionário.copy())
    del dicionário["jogador"]
for l in lista:    
    for k,v in l.items():
        print(f'O {k} {cont} tirou {v}')
        cont += 1
        sleep(0.7)
        
