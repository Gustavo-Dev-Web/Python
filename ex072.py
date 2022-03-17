extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    número = int(input('Digite um número de 0 a 20:'))
    if número <= 20 and número >= 0:
        break
    else:
        print('Tente Novamente! ', end='')
print(f'O número {número} por extenso fica {extenso[número]}')
