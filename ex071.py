saque = int(input('Digite quantos reais você quer sacar:'))
total = saque
nota = 50
contnota = 0
while True:
    if total >= nota:
        total-= nota
        contnota +=1 
    else:
        if contnota > 0:
            print(f'São {contnota} notas de {nota} reais')
        if nota == 50:
            nota = 20    
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1    
        contnota = 0    
        if total == 0:
            break       
        