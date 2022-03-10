from time import sleep

escolha = 0
maior = 0
menor = 0
acumulador = 0

while escolha != 5:
    for n in range(1,3):
        num = int(input(f'Escolha o {n}° número: '))
        acumulador += num
        if n == 1:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num 
    print('''        [1] Somar
        [2] Multiplicar
        [3] Descubra qual é o maior
        [4] Novos Números
        [5] Sair do programa''')
    escolha = int(input('Qual a sua opção? '))
    if escolha == 1:
        print(f'Sua soma é {maior + menor}')
    elif escolha == 2:
        print(f'Sua multiplicação fica {maior*menor}')    
    elif escolha == 3:
        print(f'O maior numero é {maior}')
    elif escolha > 5 and escolha < 5:
        print('Escolha uma opção correta')    