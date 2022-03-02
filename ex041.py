from datetime import date

ano_de_nascimento = int(input('Em que ano o Competidor nasceu:'))
ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento

if idade <= 9:
    print('Mirim!')
elif idade <= 14:
    print('Infantil!')
elif idade <= 19:
    print('Júnior!')        
elif idade == 20:
    print('Sênior!')
else:
    print('Master!')         