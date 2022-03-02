from time import sleep
from random import choice

sleep(0.5)
print('-=-'*20)
print('Vamos jogar pedra,papel,tesoura?')
print('-=-'*20)

jokenpo = str(input('Digite pedra,papel ou tesoura:')).strip().lower()

lista = ['pedra','papel','tesoura']
computador = choice(lista)

if jokenpo == computador:
    print('Empate')


elif computador == 'pedra' and jokenpo == 'tesoura':
    print(f'Eu ganhei!Muahahaha!Você colocou {jokenpo} e eu coloquei {computador}')
elif computador == 'pedra' and jokenpo == 'papel':
    print(f'Você ganhou!Você colocou {jokenpo} e eu coloquei {computador}')


elif computador == 'papel' and jokenpo == 'pedra':
    print(f'Eu ganhei!Muahahaha!Você colocou {jokenpo} e eu coloquei {computador}')
elif computador == 'papel' and jokenpo == 'tesoura':
    print(f'Você ganhou!Você colocou {jokenpo} e eu coloquei {computador}')


elif computador == 'tesoura' and jokenpo == 'papel':
    print(f'Eu ganhei!Muahahaha!Você colocou {jokenpo} e eu coloquei {computador}')
elif computador == 'tesoura' and jokenpo == 'pedra':
    print(f'Você ganhou!Você colocou {jokenpo} e eu coloquei {computador}')

    
else:
    print('Escolha pedra,papel ou tesoura')    