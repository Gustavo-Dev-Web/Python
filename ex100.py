from random import randint
def sorteia(lst):
    for c in range(0,5):
        lst.append(randint(0,10))
    print(f'Sorteando 5 valores da lista:',end='')
    for c in range(0,5):
        print(f' {lst[c]}',end ='')


def somaPar(lst):
    soma = cont = 0
    for c in lst:
        if lst[cont] % 2 == 0:
            soma +=lst[cont]
        cont+=1    
    print(f'\nOs valores pares da lista {lst} somados resultam em: {soma}')
numeros = []
sorteia(numeros)
somaPar(numeros)
