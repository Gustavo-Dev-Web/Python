a1 = int(input('Primeiro termo de uma PA:'))
r = int(input('Razão de uma PA:'))

a10 = a1 + 9*r
c = a1
while(c < a10+r):
    print(f'{c}', end='-> ')
    c+= r
print('acabou')    