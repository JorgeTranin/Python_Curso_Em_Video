num = int(input('Digite um numero: '))
print('Calculando o {}! ='.format(num), end=' ')
c = num
c2 = 1
for c in range(num, 0, -1):
    c2 *= c
    print(' {}'.format(c),end=' ')
    print(' x 'if c > 1 else ' = ',end='')
    c -= 1
print('{}'.format(c2))
