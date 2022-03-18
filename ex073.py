times =('Atlético Mineiro',	'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense', 'América', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport','Chapecoense')
cont = cont03 = cont04 = 0
print(f'{" POSIÇÃO NORMAL ":=^70}')
for t in times:
    print(t)
print(f'{" OS CINCO PRIMEIROS ":=^70}')
while True:
    print(f'{cont+1}° {times[cont]}')
    cont+=1
    if cont == 5:
        break
print(f'{" OS QUATRO ÚLTIMOS ":=^70}')
cont02 = 15 
while True:
    cont02+=1
    if cont02 >= 15 and cont02 < 20:
        print(f'{cont02+1}° {times[cont02]}')   
    if cont02 == 20:
        break     
print(f'{" EM ORDEM ALFABÉTICA ":=^70}')
ordem = sorted(times)
while True:
    print(f'{cont03+1}° {ordem[cont03]}')
    cont03 += 1
    if cont03 == 20:
        break
print(f'{" COLOCAÇÃO DA CHAPECOENSE ":=^70}')
print(f'A Chapecoense está na {times.index("Chapecoense")+1}° colocação.') 