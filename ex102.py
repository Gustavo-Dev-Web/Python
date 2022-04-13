def fatorial(inicio,show):
    from math import factorial
    for c in range(inicio,0,-1):
        if show:
            print(f'{c}',end=' ')
            if c > 1:
                print('x ',end='')
            else:
                print('= ',end='')    
    print(factorial(inicio)) 
    return factorial(inicio)
fatorial(inicio=6,show=False)            
