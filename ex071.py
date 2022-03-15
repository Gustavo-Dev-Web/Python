saque = int(input('Digite quantos reais você quer sacar:'))
total = saque
nota = 50
contnota = 0
while True:
    if total >= nota:
        total-= nota
        contnota +=1 
    elif resto >= 20:
        resto = saque%20
        result01 = saque//20
    elif resto >= 10:
        resto = saque%10
        result02 = saque//10
    elif resto >=1:
        resto = saque%1   
        result03 = saque//1
print(f'''Você vai sacar {result} notas de 50 reais
{result01} notas de 20 Reais
{result02} notas de 10 Reais
{result03} notas de 1 real''')         
