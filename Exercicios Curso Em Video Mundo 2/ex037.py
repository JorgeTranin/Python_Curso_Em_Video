
print('\33[31m-=-'*20)
print(' tranfomador de numeros para binarios, octal e hexa...')
print('-=-'*20)

nun = int(input('\33[mDigite um numero! '))
n = int(input(' 1 para binario, 2 para octa e 3 para hexa: '))

if n == 1:
    b = bin(nun)
    print('O numero {} em binario é {}.'.format(nun, b))
elif n == 2:
    o = oct(nun)
    print('O numero {} em octa é {}'.format(nun, o))
elif n == 3:
    hexa = hex(nun)
    print('o numero {} em hexa {}'.format(nun, hexa))

