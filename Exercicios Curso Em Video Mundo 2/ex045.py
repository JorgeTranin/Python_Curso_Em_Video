import time
from random import randint
print('\33[35m-=-\33[m'*20)
print('{:^70}'.format('\33[4;36mJOGO PEDRA  PAPEL TESOURA\33[m'))
print('\33[35m-=-\33[m'*20)

print('''Escolha:
[0] pedra
[1] papel
[2] tesoura''')
jo = int(input('Sua escolha é?'))
item = ('Pedra', 'Papel', 'Tesoura')
pc = randint(1, 2)

print('=' * 30)
print('O computador jogou {}'.format(item[pc]))
print('O jogador jogou {}'.format(item[jo]))
print('=' * 30)

if jo == pc:
    print('Empate')
elif jo == 0 and pc == 1 or jo == 1 and pc == 2 or jo == 2 and pc == 0:
    print('PC ganhou')
elif jo == 0 and pc == 2 or jo == 1 and pc == 0 or jo == 2 and pc == 1:
    print('Jogador ganhou')
