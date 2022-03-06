n = 0
o = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro:'))
    if num % 2 == 0:
        n += num
        o += 1
print(f'A soma de {o} números impares é {n}')
        