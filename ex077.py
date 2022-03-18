palavras =('amo', 'imaginar', 'nos', 'dois', 'juntos', 'pra', 'sempre', 'Gustavo', 'De', 'Moura', 'Silva',)
cont = 0
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p.lower():
        if letra in 'aeiou':
            print(letra,end='')
