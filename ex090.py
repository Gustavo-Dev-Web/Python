dicionário = {}
dicionário['nome'] = str(input('Digite o nome do Aluno:'))
dicionário['média'] = float(input('Digite a média do Aluno:'))
if dicionário['média'] < 6:
    print(f'O aluno {dicionário["nome"]} foi reprovado ')
else:
    print(f'O aluno {dicionário["nome"]} foi aprovado')    
    