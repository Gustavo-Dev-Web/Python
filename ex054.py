from datetime import date

AnoAtual = date.today().year
contmenor = 0
contmaior = 0

for pessoa in range(1, 8):
    AnoDeNascimento = int(input(f'Em que ano {pessoa}ª nasceu? '))
    idade = AnoAtual-AnoDeNascimento

    if idade < 21:
        contmenor += 1
    else:
        contmaior +=1    
print(f'Ao todo tivemos {contmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {contmenor} pessoas menores de idade')

