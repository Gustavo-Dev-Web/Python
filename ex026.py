frase = str(input('Coloque uma frase qualquer:')).strip().lower()
phrase = frase.replace(' ','')
a = frase.count('a')

print(f'A letra "A" aparece {a} vezes!')
print(f'A letra "A" aparece primeiramente na {phrase.find("a")+1}° posição da frase!')
print(f'A letra "A" aparece por último na {phrase.rfind("a")+1}° da frase!')
