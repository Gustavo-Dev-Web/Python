lista_geral = []
lista_secundária = []
lista_terciária = []
cont = 0
while True:
    nome = str(input('Nome:'))
    peso = int(input('Peso:'))
    lista_geral.append(nome)
    lista_geral.append(peso)
    lista_secundária.append(lista_geral[:])
    lista_terciária.append(lista_geral[:][1])
    lista_geral.clear()
    opção = str(input('Quer continuar?[S/N]')).strip().lower()[0]
    cont+=1
    if opção == 'n':
        break
cont2 = 0
for l in range(0,len(lista_terciária)):
    while lista_secundária[cont2][1] == max(lista_terciária):
        print(max(lista_terciária))
        cont2 += 1
print(f'Existem {cont} pessoas nessa lista')
