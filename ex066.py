n = acum = 0
while True:
    n = int(input('Digite um número [999 encerra]: '))
    if n == 999:
        break
    acum += n
print(f'A soma foi {acum}')    
