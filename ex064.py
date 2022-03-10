num = 0
acumulador=0
contador = 0
while num != 999:
    num = int(input('Digite aqui seus números(Para parar digite 999):'))
    contador+=1
    acumulador+= num
print(f'Você digitou {contador-1} números e a soma entre eles foi {acumulador-999} (Desconsiderando o 999)')    