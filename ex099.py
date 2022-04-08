def maior(*lst):
    cont = 0
    print('--'*35)
    print('Analisando os valores passados...')
    for c in range(0,len(lst)):
        print(lst[c],end=', ')
    if len(lst) > 0:    
        maxi = max(lst)    
    else:
        maxi = 0    
    print(f'foram passados {len(lst)} valores e o maior deles é {maxi}')
    cont+=1
maior(1,3,5,1,5,6,10)
maior(1,5,1)
maior()
