'''Exercício Python 074: Crie um programa que vai gerar
 cinco números aleatórios e colocar em uma tupla. Depois disso,
  mostre a listagem de números gerados e também indique o menor
   e o maior valor que estão na tupla.'''

from random import randint 


sorteio = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os numeros sorteados são:' ,end='')
maior = 0
menor = 999
for n in sorteio:
    print(f'{n}' , end=' ' )

'''for n in sorteio:
    
    if n > maior :
        maior = n
    elif n < menor:
        menor = n
'''

print(' ')
print(f' O maior valor é {max(sorteio)}')
print(f' O menor valor é {min(sorteio)}')






