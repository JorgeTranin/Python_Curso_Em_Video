'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida
   com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número
   pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''


extenso = ('zero','um','dois', 'tres', 'quatro', 'Cinco', 'Seis', 'sete', 'oito',' nove', 'dez')

while True:
    user = int(input('Digite um numero entre 0 a 10: '))
    if user > 10 or user < 0:
        print('Digite novamente')
    else:
        print(extenso[user])
        break;