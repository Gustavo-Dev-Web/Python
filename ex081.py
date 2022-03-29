lista = []
while True:
    opção = 'S'
    número = int(input(f'Digite um número:'))
    lista.append(número)
    if opção == 'S':
        opção = str(input('Quer continuar?[S/N]:'))[0].upper().strip()
    if opção != 'S' and opção != 'N':
           opção = str(input('Escolha uma opção válida...Quer continuar?[S/N]:'))
    if opção == 'N':
        break
decres =sorted(lista,reverse = True) 
print(f'Você digitou {len(lista)} números') 
print(f'A lista em forma descrescente fica: {decres}')
if 5 in lista:
    print('Essa lista tem o 5 em sua composição')
elif 5 not in lista:
    print('Essa lista não tem o 5 na sua composição')    
