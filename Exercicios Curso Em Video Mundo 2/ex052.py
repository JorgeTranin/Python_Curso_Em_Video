nun = int(input('Digite um numero: '))
tot = 0
for c in range(1, nun + 1):
    if nun % c == 0:
        print('\33[34m',end='')
        tot += 1
    else:
        print('\33[31m',end='')
    print('{}'.format(c),end='')
print('\n\33[mO numero {} foi divizivel {} vezes. '.format(nun, tot))
if tot == 2:
    print('O numero {} é primo.'.format(nun))
else:
    print('O numero {} não é primo.'.format(nun))
