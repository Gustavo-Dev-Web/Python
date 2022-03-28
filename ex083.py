expressão = str(input('Coloque sua expressão (coloque todas as pontuações):'))

c = expressão.count('(')
d = expressão.count(')')
e = expressão.count(')(')
g = expressão.count('((')
h = expressão.count('))')
i = expressão.count('()')
f = c+d

if f % 2 == 0 and e < 1 and h < 0 and g < 0 and i < 0 :
    print('Sua expressão é válida')
elif  e > 0 or g > 0  or h > 0  or i > 0 :
    print('Sua expressão não é válida')
else:
    print('Sua expressão não é válida')
