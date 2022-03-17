a = float(input('Reta 1 do triângulo:'))
b = float(input('Reta 2 do triângulo:'))
c = float(input('Reta 3 do triângulo:'))

if a < b + c and b < a + c and c < a + b:
    print('Suas retas podem formar um triângulo!')
else:
    print('Suas retas não podem formar um triângulo.')
    