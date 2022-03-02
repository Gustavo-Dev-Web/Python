from dataclasses import replace
número = int(input('Digite o número 1 pra converter pra binário o 2 pra converter pra hexadecimal e o 3 pra octal:'))

if número == 1:
    binário = int(input('Coloque aqui seu número:'))
    print('Seu número convertido para binário fica:')
    print(format(binário,'b'))
elif número == 2:
    hexadecimal = int(input('Coloque aqui seu número:'))
    print(f'Seu número convertido para hexadecimal fica:')
    hexa = hex(hexadecimal)
    replace_hexa = hexa.replace('0x','')
    print(replace_hexa) 
elif número == 3:
    octal = int(input('Coloque aqui seu número:'))
    print(f'Seu número convertido pra octal fica:')
    print(format(octal,'o'))