print('''O [1] converte pra binário
O [2] converte pra hexadecimal
O [3] converte pra octal''')

número = int(input('Digite aqui:'))

num = int(input('Coloque aqui seu número:'))

if número == 1:
    print(f'O número {num} convertido para binário fica: {bin(num)[2:]}')
elif número == 2:
    print(f'O número {num} convertido para hexadecimal fica: {hex(num)[2:]}') 
elif número == 3:
    print(f'Seu número convertido fica:{oct(num)[2:]}')
else:
    print(f'Seu número é inválido, pressione [1], [2] ou [3] e tente novamente')
    