a1 = int(input('Digite o primeiro termo de uma PA:'))
r = int(input('Digite o valor da Razão:'))

ta = 1
n = 10
an = a1 + (n-1)*r
c = a1
d = an

print('Os 10 primeiros termos são:')
while(c < an+r):
    print(f'{c}', end=' -> ')
    c+= r

#A váriavel 'ta' tem esse nome por ser um Termo Adicionado
ta = n + ta
an2= a1 +(ta-1)*r

while ta != 0:
    ta = int(input('\nTermo que você deseja adicionar:'))
    for c in range(a1,an,r):
        print (f'{c}', end = ' -> ')
    while(d < an2+r):
        print(f'{d}', end=' -> ')
        d+= r