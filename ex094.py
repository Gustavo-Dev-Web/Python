lista = []
dadospessoais = {}
while True:
    dadospessoais['nome'] = str(input('Nome:')).strip()
    dadospessoais['sexo'] = str(input('Sexo [M/F]:')).strip()[0]
    dadospessoais['idade'] = int(input('Idade:'))
    lista.append(dadospessoais.copy())
    del dadospessoais
    dadospessoais = {}
    opção = str(input('Quer continuar?[S/N]: ')).strip().lower()
    if opção == 'n':
        break
cont = totidade = 0    
for d in lista[dadospessoais['idade']]:
    totidade += d
média = totidade/len(dadospessoais['idade'])
print(média)
