lista_secundária = []
lista_principal = []
lista_terciária = []
cont = 0
while True:
    lista_secundária.append(str(input('Nome:')).strip())
    lista_secundária.append(int(input('Peso:')))
    lista_principal.append(lista_secundária[:])
    lista_secundária.clear()
    opção = str(input('Quer continuar?[S/N]')).strip().lower()[0]
    cont+=1
    if opção == 'n':
        break
print('-='*40)
cont2=0
print(f'Existem {cont} pessoas nessa lista')

for p in lista_principal:
    lista_terciária.append(lista_principal[cont2][1])
    maior = max(lista_terciária)
    if p[1] == maior:
        print(lista_principal[cont2][0],end=' ')  
    cont2+=1

print(f'pesam {maior:.2f} KG e, portanto, são os mais pesados ')
cont2=0
for p in lista_principal:
    lista_terciária.append(lista_principal[cont2][1])
    menor = min(lista_terciária)
    if p[1] == menor:
        print(lista_principal[cont2][0],end=' ')
    cont2+=1    
print(f'pesam {menor:.2f} KG e, portanto, são os mais leves ')    
