maior = 0
menor = 0

for pessoa in range(1,4):
    altura = float(input(f'Altura da {pessoa}° pessoa: '))
    if pessoa == 1:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
print(f'''A maior altura é {maior}
A menor altura é {menor}''')                    