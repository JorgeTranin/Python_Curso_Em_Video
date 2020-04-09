pa = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razao da PA: '))
c = 0
mais = 10
tot = 0
print('Os termos são', end=" ")
while mais != 0:
    tot += mais
    while c <= tot:
        c += 1
        print('{}'.format(pa), end=' -> ')
        pa = pa + r
    print('PAUSA')
    mais = int(input('Quantos termos a mais? '))
print('Foram digitados um total de {} termos'.format(tot))