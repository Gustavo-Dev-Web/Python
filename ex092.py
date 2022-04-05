from datetime import datetime
previdencia = {}
previdencia['nome'] = str(input('Nome:')).strip()
nascimento = int(input('Ano de Nascimento:'))
previdencia['idade'] = datetime.now().year - nascimento
previdencia['carteira'] = int(input('N° da Carteira de Trabalho(0 não tem): '))
if previdencia['carteira'] != 0:
    previdencia['contratação'] = int(input('Ano de contratação:'))
    previdencia['salário'] = float(input('Salário:'))
    previdencia['aposentadoria'] = (previdencia['contratação'] + 35) - nascimento
print('-='*30)    
for k,v in previdencia.items():
    print(f'-{k} tem valor {v}')
