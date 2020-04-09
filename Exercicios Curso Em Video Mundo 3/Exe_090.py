'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da
estrutura na tela.

'''

ficha = {}

ficha['nome'] = str(input('Nome do anluno: '))

ficha['media'] = float(input(f'Media do aluno {ficha["nome"]}: '))

if ficha['media'] < 5:
    ficha['situação'] = 'Reprovado'

elif ficha['media'] >= 7:
    ficha['situação'] = 'Aprovado'

else:
    ficha['situação'] = 'Recuperação'

for k, v in ficha.items():
    print(f'  - {k} é igual a {v}')