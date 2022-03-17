km = float(input('Quantos km terá até o seu destino?'))

if km <= 200:
    preço = km*0.50
    print(f'O custo será de:{preço} R$')
else:
    preço = km*0.45
    print(f'O custo será de:{preço} R$')     
    