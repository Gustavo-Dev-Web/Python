from random import randint
contador = 1
computador = randint(1,10)
jogador = int(input('Escolha um número:(De 1 até 10):'))
while jogador != computador:
    contador += 1            
    if computador < jogador:
        jogador = int(input('É MENOS... Escolha outro número:'))
    if computador > jogador:
        jogador = int(input('É MAIS... Escolha outro número:'))
print(f'Parabéns,após {contador} tentativas você acertou')                           