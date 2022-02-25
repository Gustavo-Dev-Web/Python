nome = str(input('Qual seu nome?'))

separa = nome.split()

print(f'Seu nome em máiusculo fica: {nome.upper()}')
print(f'Seu nome em minuscúlo fica: {nome.lower()}')
print(f'Seu nome Tem {len(nome)-nome.count(" ")} Letras!')
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras!')
