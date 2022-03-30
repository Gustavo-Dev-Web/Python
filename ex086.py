cont = 0
lista01 = []
lista02 = []
lista03 = []
lista04 = []
while True:
    if cont <= 2:
        lista02.append(int(input(f'Digite o valor [0, {cont}]:')))
        cont+=1
    if cont >= 3 and cont < 6:
        lista03.append(int(input(f'Digite o valor [1, {cont-3}]:')))
        cont+=1
    if cont >= 6 and cont <= 9:
        lista04.append(int(input(f'Digite o valor [2, {cont-6}]:'))) 
        cont+=1
    if cont == 9:
        break
lista01.append(lista02[:])
lista01.append(lista03[:])
lista01.append(lista04[:])
cont = cont2 = 0
print('-='*32)
for c in range(0,9):
    print(f'[{lista01[cont2][cont]:^4}]',end=' ')
    cont+=1
    if c == 2 or c == 5:
        cont=0
        print()
        cont2+=1
