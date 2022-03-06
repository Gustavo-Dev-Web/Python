frase = str(input('Digite uma frase aqui e descubra se ela é um políndromo: ')).lower()

substituir = frase.replace(' ','')
reverso =''.join(reversed(substituir))

if substituir == reverso:
    print('A frase é um políndromo')
else:
    print('A frase não é um políndromo')
        