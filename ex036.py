from time import sleep
print('-=-'*20)
print('Vamos calcular o valor das suas parcelas')
print('-=-'*20)

print('Processando...')
sleep(2.5)
imóvel = float(input('Digite aqui o valor do imóvel:'))
salário = float(input('Coloque aqui seu salário:'))
anos = int(input('Coloque aqui em quantos anos você deseja pagar:'))

parcelas = imóvel/(30/100*salário)/12

if parcelas <= anos:
    print('Você poderá parcelar sua casa própria!')
else:
    print('Infelizmente você não conseguirá financiar sua casa!')    

print(f'Suas parcelas terão que ser pagas em {parcelas + 1 :.0f} anos ou {parcelas*12 +1 :.0f} meses comprometendo 30% da sua renda')