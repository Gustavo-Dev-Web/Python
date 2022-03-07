acumulador = 0
contador = 0

for c in range(1, 7):
    num = int(input(f'{c}° número inteiro:'))
    if num % 2 == 0:
        acumulador += num
        contador += 1
print(f'A soma de {contador} números PARES é {acumulador}!')
        