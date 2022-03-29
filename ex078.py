lista = []
for l in range(0,5):
    lista.append(int(input(f'Digite um valor pra posição {l}:')))    
maior = max(lista)
menor = min(lista)
print(f'O maior valor é {maior} nas posições ',end='')
for posição,valor in enumerate(lista):
    if valor == maior:
        print(f'{posição}...',end=' ')
print(f'\nO menor valor é {menor} nas posições ',end='')
for posição,valor in enumerate(lista):
    if valor == menor:
        print(f'{posição}...',end=' ')                        
    