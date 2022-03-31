lista01 = [[], [], []]
for c in range(0, 3):
    for l in range(0,3):
        lista01[c].append(int(input(f'Digite um valor [{c}, {l}]')))
print('-='*32)
acum = soma = 0
for c in range(0,3):
    for l in range(0, 3):
        print(f'[{lista01[c][l]:^4}]  ', end = '')
        if lista01[c][l] % 2 == 0:
            acum+=lista01[c][l]
    if lista01[c][2]:
        soma += lista01[c][2]
    print()
print()        
print('=-'*32)        
print(f'A soma de todos os números pares é {acum}')
print(f'A soma dos valores da 3° coluna é {soma}')
print(f'O maior valor da 2° linha é {max(lista01[1])}')
