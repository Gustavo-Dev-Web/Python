dicionário = {}
dicionário['Nome'] = str(input('Digite o nome do Aluno:'))
dicionário['Média'] = float(input('Digite a média do Aluno:'))
if dicionário['Média'] < 7:
    dicionário['Situação'] = 'Reprovado'
else:
    dicionário['Situação'] = 'Aprovado'
for k,v in dicionário.items():
    print(f'{k}: {v}')    
    