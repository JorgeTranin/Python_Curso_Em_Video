from time import sleep
from  random import randint
print('='*20)
print('Vamos Jogar PAR OU IMPAR')
print('='*20)
sleep(2)
tot = 0
co = 0
sor = randint(1, 10)
while True:
    j = str(input('Escolha PAR ou IMPAR: [P/I]')).upper().strip()[0]
    n = int(input('Escolha um valor: '))
    tot += 1
    sleep(1)
    s = n + sor
    print('Voce jogou {n} e seu pc {sor}. A soma é {s}   ')
    if j == 'P' and s % 2 == 0:
        print(f'Voce ganhou! Seu pc escolheu {sor}')
        co +=1
    elif j == 'I' and s % 2 == 1:
        print(f'Voce ganhou! Seu pc escolheu {sor}')
        co += 1
    else:
        print(f'Voce perdeu. seu pc escolheu: {sor}')
        print('~'*30)
        break

print(f'Voce jogou {tot} vezes e ganhou {co}')

