acum = menor = cont = cont1 = 0
barato = ''

while True:
    produto = str(input('Nome do produto:')).strip()
    preço = float(input('Preço do produto:R$ '))
    cont+= 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    acum += preço
    if preço > 1000:
        cont1 += 1
    escolha = 't'
    while escolha not in 'sn':
        escolha = str(input('Quer continuar?[S/N] ')).strip().lower()[0]
    if escolha == 'n':
        break    
print(f'''O total gasto na compra é {acum}
{cont1} produtos custam mais de mil reais
O produto mais barato é {barato} e você pagou R${menor :.2f} nele''')            
