num = int(input('Qual é o número que você quer transformar em fatorial? '))
c = num
f = 1
print(f'Calculando {num}! = ',end='')
while c > 0:
    print(c,end='')
    print(' x ' if c > 1 else ' = ',end='')
    f*=c
    c-=1
print(f,end='')    