a = float(input('Lado 1 do Triângulo:'))
b = float(input('Lado 2 do Triângulo:'))
c = float(input('Lado 3 do Triângulo:'))

if a + b >= c and a + c >= b and c + b >= a:
    print('É possível formar um triângulo essas retas!')
    if a == b and b == c:
        print('É um triângulo Equilátero!')
    elif a!=b and b!=c and c!=a:
        print('É um triângulo Isósceles')
    else:
        print('É um tiângulo Isósceles')
else:
    print('Não é possível formar um Triângulo.')    
