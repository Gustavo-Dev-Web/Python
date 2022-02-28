salario = float(input('Digite seu salário para calcular seu aumento:'))

aumento01 = (15/100*salario) + salario
aumento02 = (10/100*salario) + salario

if salario <= 1250:
    print(f'Seu salário passará de {salario} para {aumento01 :.2f}')
else:
    print(f'Seu salário passará de {salario} para {aumento02 :.2f}')    
