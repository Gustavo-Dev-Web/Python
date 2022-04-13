def notas(*d,sit= False):
    """         --> Função para analisar as notas e situação de vários alunos
    :param d: uma ou mais notas dos alunos
    :param sit: define se vai ser mostrada ou não a situação dos alunos,sendo o padrão iniciado com o False"""
    dicio = dict()
    dicio['tamanho'] = len(d)
    dicio['maior'] = max(d)
    dicio['menor'] = min(d)
    dicio['média'] = sum(d)/len(d)
    if sit:
        if dicio['média'] >= 7:
            dicio['situação'] = 'Boa'
        elif dicio['média'] < 6:
            dicio['situação'] = 'Ruim'
        else:
            dicio['situação'] = 'Razoavél'     
    print(dicio)

resp = notas(9,8,6,6,sit=True)
