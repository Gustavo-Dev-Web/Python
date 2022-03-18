itens = 'Lápis', 1.50, 'Caneta', 2.00, 'Borracha', 1.25, 'Mochila', 125.00, 'Corretivo', 10.00, 'Caderno', 10.50, 'Bolsinha', 20.00

contpreço = 1 
contobjeto = cont = 0
print(f"{'Listagem De Preço':-^50}")
while True:
    if contobjeto <= 12:
        print(f'{itens[contobjeto] :.<40}',end='')
        contobjeto+=2
    if contpreço <= 13:    
        print(f'R$ {itens[contpreço]:>6.2f}')
        contpreço+=2
    if contpreço == 13:
        break
print('-'*50)