preço = float(input('Valor a pagar: R$'))

print('''[1] A vista em dinheiro/cheque
[2] 1x no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input('Digite sua opção aqui:'))

if opção == 1:
    print(f'Custará R${preço-(10/100*preço)}, um desconto de 10%')

elif opção == 2:
    print(f'Pagando à vista no cartão você pagará R${preço-(5/100*preço)}, um desconto de 5%')
elif opção == 3:   
    print(f'Pagando parcelado em 2x no cartão você pagará R${preço}, o preço normal') 
elif opção == 4:    
    print(f'Pagando parcelado em 3x ou mais no cartão você pagará R${(20/100*preço)+preço}, 20% de juros')
       