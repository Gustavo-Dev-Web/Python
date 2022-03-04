from time import sleep
from random import choice

sleep(0.5)
print('-=-'*20)
print('Vamos jogar pedra,papel,tesoura?')
print('-=-'*20)

print('''[1] pra pedra
[2] pra papel
[3] pra tesoura:''')

jogador = int(input('Coloque aqui sua escolha:'))

lista = ['pedra','papel','tesoura']
itens = ('pedra','papel','tesoura')
computador = choice(lista)


if jogador == 1 and computador == 'tesoura':
    print('Você ganhou!Você colocou pedra e eu coloquei tesoura')
elif jogador == 1 and computador == 'papel':
    print('Eu ganhei!Muahahaha!Você colocou pedra e eu coloquei papel')

elif jogador == 2 and computador == 'tesoura':
    print(f'Eu ganhei!Muahahaha!Você colocou papel e eu coloquei tesoura')
elif jogador == 2 and computador == 'pedra':
    print(f'Você ganhou!Você colocou papel e eu coloquei pedra')

elif jogador == 3 and computador == 'pedra':
    print(f'Eu ganhei!Muahahaha!Você colocou tesoura e eu coloquei pedra')
elif jogador == 3 and computador == 'papel':
    print(f'Você ganhou!Você colocou tesoura e eu coloquei papel')

elif jogador != 1 and jogador != 2 and jogador != 3:
    print('Escolha uma opção válida!')

else:
    print('Empate!')    
