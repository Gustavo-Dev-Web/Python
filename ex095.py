gols = []
aglomerado = []
dados = {}
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Atleta: '))
    partidas = int(input(f'Quantas partidas o jogador {dados["Nome"]} jogou:'))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols o jogador {dados["Nome"]} fez na partida {c+1}: ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    gols.clear()
    aglomerado.append(dados.copy())
    opção = str(input('Quer continuar?[S/N]'))[0]
    if opção in 'Nn':
        break
print('\/'*35)
print('N°   Nome        Gols            Total')
print('--'*35)
for c in range(0,len(aglomerado)):
    print(f'{c}    {aglomerado[c]["Nome"]}   {aglomerado[c]["Gols"]}    {aglomerado[c]["Total"]}')
while True:    
    opção = int(input('Mostrar dados de qual jogador?[999 para] '))
    while opção > len(aglomerado)-1:
        opção = int(input(f'''Erro! Não existe jogador com código {opção}
Mostrar dados que qual jogador?[999 para] '''))
    if opção == 999:
        break
    print(f'-Levantamento do jogador {aglomerado[opção]["Nome"]}')
    for c in range(0,len(aglomerado[opção]['Gols'])):
        print(f'    No jogo {c+1} fez {aglomerado[opção]["Gols"][c]} gols')
