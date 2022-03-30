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
print('-='*40)
cont2=0
print(f'Existem {cont} pessoas nessa lista')

for p in lista_secundária:
    if p[1] == max(lista_terciária):
        print(lista_secundária[cont2][0],end=' ')
    cont2+=1    
print(f'pesam {max(lista_terciária):.2f} KG e, portanto, são os mais pesados ')
cont2=0
for p in lista_secundária:
    if p[1] == min(lista_terciária):
        print(lista_secundária[cont2][0],end=' ')
    cont2+=1    
print(f'pesam {min(lista_terciária):.2f} KG e, portanto, são os mais leves ')    
