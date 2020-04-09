'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3
e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta.

'''

matriz = [[], [], []]

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para a posição [{i}, {c}]: ')))


for i in range(0, 3):
    print('')
    for c in range(0 ,3):
        print(f'[ {matriz[i][c]:^6} ] ',end='')
