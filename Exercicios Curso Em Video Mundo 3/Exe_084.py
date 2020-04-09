'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
 guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

'''

pessoas = []
dados = []

maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
        
    elif dados[1] < menor:
        menor = dados[1]
        

    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: '))

    if resp in 'Nn':
        break
    

print(f'Um total de {len(pessoas)} pessoas foram cadastradas.')


        
print(f'O mais pesado é de {maior}.2f Kg e os nomes são ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[ {p[0]} ]', end=' ')
print(' ')
print(f'O mais leves é de {menor}.2f Kg e os nomes são ',end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[ {p[0]} ]', end=' ')



        