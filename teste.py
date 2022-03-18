listas = []
for cont in range(1,5):
    listas.append(int(input('Número:')))

for c,v in enumerate(listas):
    print(f'Na posição {c} encontrei o valor {v}')