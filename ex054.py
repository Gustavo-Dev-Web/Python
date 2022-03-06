from datetime import date

AnoAtual = date.today().year
totmenor = 0
totmaior = 0

for pessoa in range(1, 8):
    AnoDeNascimento = int(input(f'Em que ano {pessoa}ª nasceu? '))
    idade = AnoAtual-AnoDeNascimento

    if idade <= 21:
        totmenor += 1
    else:
        totmaior +=1    
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')        

