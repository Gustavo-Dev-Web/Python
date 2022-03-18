from random import randint
print(f'Os valores sorteados foram: ',end='')
aleatório = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
for a in aleatório:
    print(a,end=' ')
print(f'\nO menor valor sorteado foi: {min(aleatório)}')  
print(f'O maior valor sorteado foi: {max(aleatório)}') 
