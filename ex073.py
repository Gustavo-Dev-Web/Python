times =('Atlético Mineiro',	'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense', 'América', 'Atlético', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport','Chapecoense')

cont = cont03 = cont04 = cont05 = 0

print('='*30,end=' ')
print('POSIÇÃO NORMAL',end=' ')
print('='*30)
while True:
    print(f'{cont05+1}° {times[cont05]}')
    cont05 += 1
    if cont05 == 20:
        break

print('='*30,end=' ')
print('OS CINCO PRIMEIROS',end=' ')
print('='*30)
while True:
    print(f'{cont+1}° {times[cont]}')
    cont+=1
    if cont == 5:
        break
 
print('='*30,end=' ')
print('OS QUATRO ÚLTIMOS',end=' ')
print('='*30)
cont02 = 15 
while True:
    cont02+=1
    if cont02 >= 15 and cont02 < 20:
        print(f'{cont02+1}° {times[cont02]}')   
    if cont02 == 20:
        break     

print('='*30,end=' ')
print('EM ORDEM ALFABÉTICA',end=' ')
print('='*30)
ordem = sorted(times)
while True:
    print(f'{cont03+1}° {ordem[cont03]}')
    cont03 += 1
    if cont03 == 20:
        break

print('='*30,end=' ')
print('Colocação Da Chapecoense',end=' ')
print('='*30)   
while times[cont04] != 'Chapecoense':
    cont04 +=1   
print(f'A Chapecoense está na {cont04+1}° colocação.') 
