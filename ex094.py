lista = []
listamulher = []
listaidade = []
totidade = cont = 0
while True:
    dadospessoais = {}
    dadospessoais['nome'] = str(input('Nome:')).strip()
    while True:
        dadospessoais['sexo'] = str(input('Sexo [M/F]:')).strip()[0].upper()
        if dadospessoais['sexo'] in 'MF':
            break
        dadospessoais.pop('sexo')
    dadospessoais['idade'] = int(input('Idade:'))
    totidade += dadospessoais['idade']
    if dadospessoais['sexo'] == 'F':
         listamulher.append(dadospessoais['nome'])
    lista.append(dadospessoais.copy())
    del dadospessoais
    opção = ' '
    while opção not in 'sn':
        opção = str(input('Quer continuar?[S/N]: ')).strip().lower()
    if opção == 'n':
        for c in range(0,len(lista)):
            if lista[c]['idade'] > totidade/len(lista):
                listaidade.append(lista[c])
        break
print(f'- O grupo é formado por {len(lista)} pessoas')
print(f'- A média de idade foi:{totidade/len(lista):.2f}')
print(f'- As mulheres da lista são:',end=' ')
for c in range(0,len(listamulher)):
        print(listamulher[c],end=' ')
print('\n- As pessoas com idade acima da média são:') 
for v in enumerate(listaidade):
    print(v,end=' ')
    cont +=1
    