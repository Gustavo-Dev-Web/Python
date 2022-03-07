frase = str(input('Digite uma frase aqui e descubra se ela é um políndromo: ')).capitalize()

substituir = frase.replace(' ','')
reverso =''.join(reversed(substituir)).title()

print(f'A frase {frase} ao contrário é {reverso}')

if substituir == reverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
        