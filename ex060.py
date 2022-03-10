cont = 0

num = int(input('Qual é o número que você quer transformar em fatorial? '))
for s in range(num, 1, -1):
    multiplicação = (num*s)
    if multiplicação > 0:
        cont += multiplicação
print(f'o número {num}! fatorado fica:{cont}')