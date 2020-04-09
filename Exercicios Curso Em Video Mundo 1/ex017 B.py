from math import hypot
c = float(input('Digite o cateto: '))
ca = float(input('Digite o catedo adjacente: '))
h = hypot(c, ca)
print('A hipotenusa tem o valor de {:.2f}'.format(h))