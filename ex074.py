from random import randint
cont = maior = menor = 0
print(f'Os valores sorteados foram: ',end='')
while True:
    cont +=1
    aleatório = randint(1,10)
    if cont == 1:
        maior = menor = aleatório
    tupla = (f'{aleatório}')
    print(f'{tupla}',end=' ')
    if aleatório > maior:
        maior = aleatório 
    if aleatório < menor:
        menor = aleatório    
    if cont == 5:
        break
print(f'\nO menor valor sorteado foi: {menor}')  
print(f'O maior valor sorteado foi: {maior}')  
