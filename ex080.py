listas=[]
maior = 0
for c in range(0,5):
    valor = int(input('Digite um valor:'))
    if c == 0 or valor > listas[-1]:
        listas.append(valor)
        print('Adicionado ao último item da lista:')
    else:
        pos = 0     
        while pos < len(listas):
            if valor <= listas[pos]:
                listas.insert(pos,valor)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-='*30) 
print(f'A sua lista, em ordem crescente fica:{listas}')           