'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA
a criar palpites.O programa vai perguntar quantos jogos serão gerados e
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em
uma lista composta.

'''
from time import sleep
from random import sample
numeros_megasena = list(range(1, 61))
jogos = list()
print('='*30)
print('      Jogos da mega sena      ')
print('='*30)

n = int(input('Quantos jogos você quer gerar? '))

for i in range(0, n):
    jogos.append(sample(numeros_megasena, 6))
print('*'*40)

print(f'-======= Sorteando {len(jogos)} jogos -=========')
print('*'*40)
sleep(2)
for c, j in enumerate(jogos) :
    j.sort()
    sleep(1)
    print(f'Jogo {c+1}: {j}')