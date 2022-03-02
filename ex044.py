preço = float(input('Valor a pagar:'))
opção = input('Digite 1 pra cartão e 2 dinheiro/cheque:')

dinheiro = (10/100)*preço
parcela = (20/100)*preço

if opção == 2:
    print(f'Caso pague à vista, custará {preço-dinheiro}, um desconto de 10%')

if opção == 1:
    cartão = int(input('Digite 1 pra parcelamento ou 2 pra pagamento a vista'))
if cartão == 1:
    print(f'Caso parcele em 2x você terá de pagar {preço}, o preço normal')
    print(f'Caso parcele em 3x você terá de pagar {preço+parcela}, 20% de juros')
elif cartão == 2:
    print(f'Caso pague à vista pagará {preço-(5/100*preço)}, um desconto de 5%')        