acumulador = 0
MaisVelho = 0
contador = 0
NomeDoMaisVelho = ''

for p in range(1,5):
    print(f'-----{p}ª PESSOA-----')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).lower().strip()
    acumulador += idade
    if p == 1 and sexo in 'Mm':
        MaisVelho = idade 
        NomeDoMaisVelho = nome   
    if idade > MaisVelho and sexo == 'm':
        MaisVelho = idade
        NomeDoMaisVelho = nome
    if idade < 20 and sexo == 'f':
        contador += 1    

print(f'A média de idade é:{acumulador/4}')    
print(f'A idade do homem mais velho é {MaisVelho} e o nome dele é {NomeDoMaisVelho}')
print(f'Existem {contador} mulheres com menos de 20 anos')