from random import randint
cont = 0
while True:
    comp = randint(1,10)
    n = int(input('Escolha seu número:'))
    opção = str(input('Par ou ímpar:[P/I] ')).lower().strip()
    tot = n + comp
    print('-=-'*20)
    if opção == 'p':
        if tot % 2 == 0:
            print(f'Você ganhou!', end='')
            cont += 1
        else:
            print(f'Você perdeu!',end='')  
            break     
    elif opção == 'i':
        if tot % 2 != 0:
            print(f'Você ganhou!',end='')
            cont += 1
        else:
            print(f'Você perdeu!',end='') 
            break       
    print(f'Você colocou {n} e eu {comp}') 
    print('-=-'*20)   
print(f'Você ganhou {cont} vezes!')
print('-=-'*20)