while True:
    print('-'*70)
    n = int(input('A tabuada de qual número você quer? '))
    if n < 0:
        break
    print('-'*70)
    for t in range(1,11):
        print(f'{n} x {t} = {t*n}')
