from time import sleep
escolha = 0
maior = 0
menor = 0
n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
sleep(1)
while escolha != 5:  
    print('-=-'*20)          
    print('''[1] Somar
[2] Multiplicar
[3] Descubra qual é o maior
[4] Novos Números
[5] Sair do programa''')
    sleep(1)
    escolha = int(input('----> Qual a sua opção? '))
    sleep(1)
    if escolha == 1:
        print('-=-'*20)
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    elif escolha == 2:
        print('-=-'*20)
        print(f'Sua multiplicação fica {n1*n2}')    
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('-=-'*20)    
        print(f'O maior entre {n1} e {n2} é {maior}')       
    elif escolha == 4:
        print('Escolha novamente seus números')
        n1 = int(input('Primeiro número:'))
        n2 = int(input('Segundo número:'))   
                