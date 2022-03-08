frase = str(input('Digite uma frase aqui e descubra se ela é um palíndromo: ')).upper()

substituir = frase.replace(' ','')

juntando=''.join(substituir)
reverso = juntando[::-1]
print(f'A frase {substituir} ao contrário é {reverso}')

if substituir == reverso:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
        