def voto(anodeNasc):
    from datetime import datetime
    idade = datetime.now().year - anodeNasc
    if idade < 16:
        cond = f'Com {idade} anos:Voto Negado'
    elif idade > 18 and idade < 65:
        cond = f'Com {idade} anos: Voto Obrigatório'
    else:
        cond = f'Com {idade} anos:Voto Opcional'
    return cond
v= int(input('Ano De Nascimento:'))
print(voto(v))
