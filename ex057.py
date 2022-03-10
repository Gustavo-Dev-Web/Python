s = ''

s = str(input('Seu sexo é masculino ou feminino? [M/F] ')).lower()[0]

while s != 'm' and s != 'f':
    print('Informe corretamente por favor!')
    s = str(input('Seu sexo é masculino ou feminino? [M/F] ')).lower()

