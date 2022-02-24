dias = int(input('Quantos dias você dirigiu:'))
km = float(input('Quantos Quilomêtros você rodou:'))

custo01 = dias*60
custo02 = km*0.15

print(f'Você pagará {custo01} R$ pelos dias,mais {custo02 :.2f} R$ pelos Quilômetros,totalizando {custo01+custo02 :.2f} R$')