from random import randint
while True:
    comp = randint(1,10)
    n = int(input('Escolha seu número:'))
    opção = str(input('Par ou ímpar:[P/I] ')).strip().lower()[0]
    if n + comp % 2 == 0:
        if opção in 'Pp':
            print(f'Você ganhou! eu coloquei {comp} e você colocou {n}')
        elif opção in 'Ii':
            print(f'Você perdeu! eu coloquei {comp} e você colocou {n}')   
    elif n + comp % 2 > 0:
        if opção in 'Ii':
            print(f'Você ganhou! eu coloquei {comp} e você colocou {n}')
        elif opção in 'Pp':
            print(f'Você perdeu! eu coloquei {comp} e você colocou {n}')    
