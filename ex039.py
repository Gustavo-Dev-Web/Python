from datetime import date

AnoDeNascimento = int(input('Em qual ano você nasceu? '))

AnoAtual = date.today().year
idade = AnoAtual - AnoDeNascimento
TempoParaMaioridade = 18 - idade
TempoDeMaioridade = idade - 18

if idade < 18:
    print(f'Você ainda se alistará em {TempoParaMaioridade} ano(s)!')
    print(f'Você terá que se alistar em {AnoAtual + TempoParaMaioridade}')
elif idade > 18:
    print(f'Você deveria ter se alistado em {TempoDeMaioridade} ano(s)!')
    print(f'Você deveria ter se alistado em {AnoAtual - TempoDeMaioridade }')
elif idade == 18:
    print('Você está no ano de alistamento!')    
    