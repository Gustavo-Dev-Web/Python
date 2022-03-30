lista_02 = []
lista_03 = []
lista_01 = []
for c in range(1,8):
    numero = int(input(f'Digite o {c}° número:'))
    if numero % 2 == 0:
        lista_02.append(numero)
    elif numero % 2 > 0:
        lista_03.append(numero) 
lista_01.append(lista_02[:])
lista_01.append(lista_03[:])          
print(f'Os números pares são: {sorted(lista_01[0])}')
print(f'Os números ímpares são: {sorted(lista_01[1])}')
