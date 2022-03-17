from time import sleep
print('-=-'*20)
print('Vamos calcular o valor das suas parcelas')
print('-=-'*20)

print('Processando...')
sleep(1)
imóvel = float(input('Digite aqui o valor do imóvel:'))
salário = float(input('Coloque aqui seu salário:'))
anos = int(input('Coloque aqui em quantos anos você deseja pagar:'))

minímo = salário*(30/100)
parcelas = imóvel/(anos*12)

print(f'Para pagar uma casa de R${imóvel} em {anos} anos suas parcelas seriam de R$ {parcelas}')
if parcelas <= minímo:
    print('Você poderá parcelar sua casa própria!')
elif parcelas > minímo:
    print('Infelizmente você não conseguirá financiar sua casa!')
    