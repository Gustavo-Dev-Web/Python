extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete', 'dezoito', 'dezenove', 'vinte'
opção = ' '
while True:
    número = int(input('Digite um número de 0 a 20:'))
    if número > 20 :
        número = int(input('Tente Novamente!Digite um número de 0 a 20: '))  
    if número < 0 :
        número = int(input('Tente Novamente!Digite um número de 0 a 20: '))      
    print(f'O número {número} por extenso fica {extenso[número]}')
    while opção not in 'sn':
        opção = str(input('Quer continuar?[S/N]:')).strip().lower()    
    if opção == 'n':
        break
    opção = ' '