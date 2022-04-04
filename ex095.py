gols = []
dados = {}
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Atleta: '))
    partidas = int(input('Quantas partidas o jogador jogou:'))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols o jogador {dados["Nome"]} fez na partida {c}: ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    gols.append(dados.copy())
    opção = str(input('Quer continuar?[S/N]'))[0]
    if opção in 'Nn':
        break
print('--'*30)
print(gols)
