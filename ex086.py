lista01 = [[], [], []]
for c in range(0, 3):
    for l in range(0,3):
        lista01[c].append(int(input(f'Digite um valor [{c}, {l}]')))
print('-='*32)
for c in range(0,3):
    for l in range(0, 3):
        print(f'[{lista01[c][l]:^4}]  ', end = '')
    print()
