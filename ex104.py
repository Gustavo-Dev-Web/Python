def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num)) 
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:    
            print('\033[0;31mErro, Digite um número válido!\033[m')
        if ok:
            break
    return valor    
n = leiaInt('Número:')
print(f'Você digitou o valor {n}')
