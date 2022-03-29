lista01=[]
lista02=[]
lista03=[]
while True:
    opção = 'S'
    núm = int(input('Digite um valor:'))
    lista01.append(núm)
    if opção == 'S':
        opção = str(input('Quer continuar?[S/N]:'))[0].upper().strip()
    if opção != 'S' and opção != 'N':
           opção = str(input('Escolha uma opção válida...Quer continuar?[S/N]:'))       
    if opção == 'N':
        break
print('-='*30)
for c in range(0,len(lista01)):
      if lista01[c] % 2 == 0:
          lista02.append(lista01[c])
      else:
          lista03.append(lista01[c])
print(f'A lista completa é:{lista01}')
print(f'A lista só de pares é:{lista02}')
print(f'A lista só de ímpares é:{lista03}')               
