from time import sleep
def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1 
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')    
    if inicio > fim and passo >0:
        passo = -(passo)   
    if passo < 0:
        fim -=1
    elif passo >0:
        fim += 1           
    for c in range(inicio,fim,passo): 
        print(c,end=' ',flush=True)
        sleep(0.5)            
contador(1,10,1)
print()
contador(10,0,-2)
print()
print('--'*35)
contador(inicio = int(input('Inicio: ')),fim = int(input('Fim: ')),passo = int(input('Razão: ')))
