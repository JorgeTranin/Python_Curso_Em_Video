from random import randint
from time import sleep
print('Pensei em um numero...')
pc = randint(0,5)
n = int(input('Digite um numero de 0 a 5: '))
print('PROCESSANDO...')
sleep(2)
if n == pc:
    print('Você ganhou.')
else:
    print('Você nao ganhou.')
    print('O numero que o pc escolheu foi {}'.format(pc))
