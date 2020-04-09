'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem
um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário em Python. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.

'''

from random import randint
from time import sleep
from operator import itemgetter
resultados =    {'jogador1': randint(1, 6),
                'jogador2': randint(1, 6),
                'jogador3': randint(1, 6),
                'jogador4': randint(1, 6),}

ranking = []
print('       Sorteando....       ')

for k, v in resultados.items():
    print(f'O {k} tirou {v}')
    sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print('****** O Ranking  *********')

for i, v in enumerate(ranking):
    print(f'{i+1}º colocado foi {v[0]} com {v[1]}')
    sleep(1)



'''print('       Sorteando....       ')
for i in range(0,4):
    resultados['Nome'] = 'jogador'
    print(f'O jogador {i+1}  ', end=' tirou ')
    resultados['result'] = randint(1, 6)
    print(f'{resultados["result"]} ')
    aux.append(resultados.copy())
    sleep(1)
print('-='*40)
print('***** Ranking de campeões *******')

rankin = {}


for i in range(0, 4):
    
    sleep(1)
    print(f'{i+1}º Lugar: ', aux[i] ['Nome'], end=' com ')
    print(aux[i] ['result'])

'''



   

