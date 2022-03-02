from datetime import date

ano_de_nascimento = int(input('Em qual ano você nasceu? '))

ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento
tempo_para_maioridade = 18 - idade
tempo_de_maioridade = idade - 18

if idade < 18:
    print('Você ainda se alistará!')
    print(f'Você terá que se alistar em {ano_atual + tempo_para_maioridade}')
elif idade > 18:
    print('Já passou o tempo para se alistar')
    print(f'Você deveria ter se alistado em {ano_atual - tempo_de_maioridade }')
elif idade == 18:
    print('Você está no ano de alistamento!')    