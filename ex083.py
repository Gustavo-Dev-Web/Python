pilha = []
expressão = str(input('Digite a sua expressão:'))
for símbolo in expressão:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo==')':
        pilha.pop()  
if len(pilha) > 0:
    print(f'Sua expressão {expressão} não é válida!')
elif len(pilha) == 0:
    print(f'Sua expressão {expressão} é válida!')           
