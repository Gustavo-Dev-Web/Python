peso = float(input('Você pesa quantos quilos? '))
altura = float(input('Você mede quantos metros? '))

imc = peso/altura**2

if imc < 18.5:
    print(f'Seu IMC é {imc :.1f}, você está Abaixo do Peso!')
elif imc >= 18.5 and imc < 25.0:
    print(f'Seu IMC é {imc :.1f}, você está No peso Normal')
elif imc >= 25.0 and imc < 30: 
    print(f'Seu IMC é {imc :.1f}, você está Um pouco acima do Peso!')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é {imc :.1f}, você está Acima do Peso')
else:
    print(f'Seu IMC é {imc :.1f}, você está com Obesidade Mórbida')             
      