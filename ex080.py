listas=[]
maior = 0
for c in range(0,5):
    va = int(input('Digite um valor:'))
    if c == 0 or va > listas[-1]:
        listas.append(va)
        print('Adicionado ao último item da lista:')
    else:
        pos = 0     