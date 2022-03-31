lista01 = []
while True:
    nome = input('Nome do Aluno:')
    nota01 = float(input('Nota 1:'))
    nota02 = float(input('Nota 2:'))
    lista01.append([nome, [nota01,nota02]])
    opção = str(input('Quer continuar?[S/N] '))
    if opção == 'n':
        break
cont = 0
print('-='*35)
print(f'{"N°":<4}{"Nome":<10}{"Média":<8}')
print('--'*35)
for c in range(0,len(lista01)):
    média = lista01[cont][1][0] + lista01[cont][1][1]
    print(f'{c:<4}{lista01[cont][0]:<10}{média/2:<8.2f}')
    cont+=1
print('--'*35)    
while True:
    número = int(input('Escolha o número do aluno (999 interrompe):'))
    if número == 999:
        break
    print(f'As notas de {lista01[número][0]} são: {lista01[número][1][0]} e {lista01[número][1][1]}')
