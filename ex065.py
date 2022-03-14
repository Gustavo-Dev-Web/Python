opção = ''
maior = menor = acum = cont = num = 0

while opção != 'n':
    num = int(input('Digite um número:'))
    opção=str(input('Quer continuar?[S/N]:'))  
    acum += num  
    cont+= 1
    if cont == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
            
print(f'''A média é {acum/cont :.1f}
O {maior} foi o maior número digitado
O {menor} foi o menor número digitado''')
