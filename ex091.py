from random import randint
from time import sleep
from operator import itemgetter
ranking = []
dicionário = {}
for c in range(0,4):
    dicionário[f"jogador {c+1}"] = randint(1,6)
for k,v in dicionário.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('                            Posição dos Jogadores')    
ranking = sorted(dicionário.items(),key= itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º {v[0]} com {v[1]}')
    sleep(1)
