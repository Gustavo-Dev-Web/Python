preço = float(input('Valor a pagar:'))
opção = int(input('Digite 1 pra cartão e 2 dinheiro/cheque:'))

if opção == 2:
    print(f'Caso pague à vista, custará {preço-(10/100*preço)}, um desconto de 10%')

if opção == 1:
    print(f'Pagando à vista no cartão você pagará {preço-(5/100*preço)}, um desconto de 10%')
    print(f'Pagando parcelado em 2x no cartão você pagará {preço}, o preço normal') 
    print(f'Pagando parcelado em 3x ou mais no cartão você pagará {(20/100*preço)+preço}, 20% de juros')
       