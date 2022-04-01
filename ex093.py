dados = {}
gols = []
golstot = cont = 0
dados['Nome'] = str(input('Nome do Atleta:'))
partidas = int(input('Quantas partidas o jogador jogou:'))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols o jogador {dados["Nome"]} fez na partida {c}: ')))
    dados['gols'] = gols[:]
for g in gols:
    golstot += g
dados['total'] = golstot
print('--'*30)    
print(dados)
print('--'*30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('--'*30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'        => Na partida {c}, fez {dados["gols"][c]} gols')
print(f'Foi um total de {dados["total"]} gols')    
