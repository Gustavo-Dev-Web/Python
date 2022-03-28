lista = []
for l in range(0,5):
    lista.append(int(input(f'Digite um valor pra posição {l}:')))    
    if l == 0:
        maior=menor=lista[l]
    else:
        if lista[l] > maior:
            maior = lista[l]
        if lista[l] < menor:
            menor= lista[l]
print(f'O maior valor é {maior} nas posições ',end='')
for posição,valor in enumerate(lista):
    if valor == maior:
        print(f'{posição}...',end=' ')
print(f'\nO menor valor é {menor} nas posições ',end='')
for posição,valor in enumerate(lista):
    if valor == menor:
        print(f'{posição}...',end=' ')                        
    