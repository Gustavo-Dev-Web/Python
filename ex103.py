def ficha(jogador,gols): 
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '' or gols.isalpha() or gols.isascii():
        gols = 0    
    print(f'O jogador {jogador} fez {gols} Gol(s)') 

j = str(input('Jogador: '))
g = str(input('Gols: '))
if g.isnumeric():
   g = int(g)
ficha(j,g)
