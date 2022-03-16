M = ContF = cont = 0
while True:
    idade = int(input('Idade:'))
    sexo = 't'
    while sexo not in 'mf':
        sexo = str(input('Sexo:[M/F] ')).lower().strip()[0]
    if idade > 18:
        cont+=1
    if sexo in 'f' and idade < 20:
            ContF+= 1
    if sexo in 'm':
        M += 1  
    escolha = 't'    
    while escolha not in 'sn':    
        escolha = str(input('Quer continuar?[S/N]:'))  
    if escolha == 'n':
        break    
print(f'''Tem {ContF} mulheres com menos de 20 anos
Ao todo são {M} homens cadastrados
Tem {cont} pessoas com mais de 18 anos''')    
