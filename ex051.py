a1 = int(input('Primeiro termo da PA:'))
r = int(input('Razão da PA:'))
an = a1 + (9*r)
for c in range(a1, an, r):
    print(c, end=' → ')
print('Acabou')    
