dados = {}
gols = []
dados['Nome'] = str(input('Nome do Atleta:'))
partidas = int(input('Quantas partidas o jogador jogou:'))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols o jogador {dados["Nome"]} fez na partida {c}: ')))
    dados['Gols'] = gols[:]
dados['Total'] = sum(gols)
print('--'*30)    
print(dados)
print('--'*30)
for k,v in dados.items():
    print(f'{k}: {v}')
print('--'*30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'        => Na partida {c}, fez {dados["Gols"][c]} gols')
print(f'Foi um total de {dados["Total"]} gols')    
