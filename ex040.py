nota01 = float(input('Nota 01: '))
nota02 = float(input('Nota 02: '))

média = (nota01 + nota02)/2

print(f'A média entre {nota01 :.2f} e {nota02 :.2f} é: {média :.2f}')

if média < 5.0:
    print('Reprovado!')
if média >= 7.0:
    print('Aprovado!')
else:
    print('Recuperação!')        