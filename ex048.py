n = 0
o = 0
for c in range(1, 501, 2):
    if c % 3 == 0: 
        n += c
        o += 1
print(f'A soma dos números é {n}')