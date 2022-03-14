a1 = int(input('Primeiro termo de uma PA:'))
r = int(input('Razão de uma PA:'))

termo = a1
c=1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo}',end='')
        termo += r
        print(' -> ',end='')
        c+=1  
    mais = int(input('\nQuantos termos você quer mostrar a mais: '))
    print(' -> ' if mais > 0 else '', end='')      
        