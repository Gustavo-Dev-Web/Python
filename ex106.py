def ajuda(c):
    titulo('Acessando o PyHelp',2)
    print(help(c))


def titulo(msg,cor=0):
    # 0=reset,1=preto, 2=vermelho, 3=verde, 4=amarelo, 5=azul, 6=magenta, 7=ciano
    cores = ['\033[0;0m','\033[1;40m','\033[1;41m','\033[1;42m','\033[1;43m','\033[1;44m','\033[1;45m','\033[1;46m']
    print(cores[cor])
    print('-'*(len(msg)+4))
    print(f'  {msg}  ')
    print('-'*(len(msg)+4))
    print(cores[0])


while True:
    titulo('Definição de Biblioteca',7)
    comando = (str(input('Função ou biblioteca:')))   
    if comando.upper() == 'FIM':
        titulo('Até Logo')
        break
    ajuda(comando)
