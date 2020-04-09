from random import randint
from time import sleep
sorteio = randint(1, 10)
print('---------- Vou sortear um numero -------')
sleep(2)
print('Pronto.... tente advinhar')
j = 1
cont = 0
while j != sorteio:
    print('' )
    j = int(input('Qual numero vc escolhe? '))
    print(' ')
    sleep(1)
    if j != sorteio:
        print('Tente outro numero :(')
        cont += 1
print('-=-'*25)
print('Você acertou, PARABENS.')
print('Voce precisou de {} PALPITES.'.format(cont + 1))
