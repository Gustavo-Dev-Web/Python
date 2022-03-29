lista = []
while True:
    v = (int(input(f'Digite um número:')))
    if v not in lista:
        print('Valor adicionado...')
        lista.append(v)
    else:
        print('O valor está duplicado,não irei adicionar...')    
    condição = str(input('Quer continuar?[S/N]:')).strip()[0].lower()
    if condição != 's' and condição != 'n':
        condição = str(input('Opção inválida...Quer continuar?[S/N]:')).strip().lower()[0]
    if condição == 'n':
        break    
print('-=-'*35)    
print(sorted(lista))
