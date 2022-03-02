nota01 = float(input('Nota 01: '))
nota02 = float(input('Nota 02: '))

média = (nota01 + nota02)/2

if média < 5.0:
    print('Reprovado!')
if média >= 7.0:
    print('Aprovado!')
else:
    print('Recuperação!')        