pa = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
c = 0
print('Os termos são', end=" ")
while c < 10:
    c += 1
    print('{}'.format(pa), end=' -> ')
    pa = pa + r
print('FIM')
