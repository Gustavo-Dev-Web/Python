vel = float(input('Qual era a velocidade do carro?(km/h) '))
multa = (vel - 80)*7

if vel <= 80:
    print('Sua velocidade está no limite,parabéns!')
else:
    print(f'Você ultrapassou o limite de velocidade,sua multa será de {multa}R$ !')    
