num = acum = cont = 0
while num != 999:
    num = int(input('Digite aqui seus números(Para parar digite 999):'))
    if num != 999:
        cont+=1
        acum+= num
print(f'Você digitou {cont} números e a soma entre eles foi {acum} (Desconsiderando o 999)')    