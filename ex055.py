maior = 0
menor = 0

for pessoa in range(1,6):
    peso = float(input(f'Peso da {pessoa}ª pessoa:KG '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é: {maior}')
print(f'O menor peso é: {menor}')                    
