from random import randint
cont = 0
while True:
    opção = 'w'
    comp = randint(1,10)
    n = int(input('Escolha seu número:'))
    while opção not in 'pi':
        opção = str(input('Par ou ímpar:[P/I] ')).lower().strip()
    print(f'Você jogou {n} e o computador jogou {comp}')    
    tot = n + comp
    if opção == 'p':
        if tot % 2 == 0:
            cont += 1
            print('Você venceu!')
        else:
            print('Você perdeu!',end='')
            break     
    elif opção == 'i':
        if tot % 2 != 0:
            cont += 1
            print('Você venceu!')
        else:
            print('Você perdeu!',end='')
            break  
print('-=-'*20)
print(f'Você ganhou {cont} vezes!')
print('-=-'*20)
