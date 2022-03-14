M = ContF = cont = 0
escolha = 's'
sexo = ''
while escolha =='s':
    idade = int(input('Idade:'))
    sexo = str(input('Sexo:[M/F] ')).lower().strip()
    if idade > 18:
        cont+=1
    if sexo in 'f':
        if idade < 20:
            ContF+= 1
    if sexo in 'm':
        M += 1  
    escolha = str(input('Quer continuar?[S/N]:'))  
print(f'''Tem {ContF} mulheres com menos de 20 anos
Ao todo são {M} homens cadastrados
Tem {cont} pessoas com mais de 18 anos''')    
