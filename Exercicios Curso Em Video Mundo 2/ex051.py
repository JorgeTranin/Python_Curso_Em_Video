p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
d = p + (10-1)*r
for c in range(p, d + r, r):
    print(c, end='->')
print('Fim')