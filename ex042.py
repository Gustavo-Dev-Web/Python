a = float(input('Lado 1 do Triângulo:'))
b = float(input('Lado 2 do Triângulo:'))
c = float(input('Lado 3 do Triângulo:'))

if a + b > c and c + a > b and c + b > a:
    print('É possível formar um triângulo essas retas!')
else:
    print('Não é possível formar um triângulo com essas retas')

if a == b and b > c:
    print('É um triângulo Isósceles!')  
elif a == b and b < c:
    print('É um triângulo Isósceles!')
elif a == c and c > b:
    print('É um triângulo Isósceles!')
elif a == c and c < b:
    print('É um triângulo Isósceles!')

if a == b and b == c:
    print('É um triângulo Equilátero!')

if a != b and b != c:
    print('É um triângulo Escaleno!')        