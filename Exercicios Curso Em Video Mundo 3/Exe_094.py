'''
Exercício Python 094: Crie um programa que leia nome,
sexo e idade de várias pessoas, guardando os dados de
cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre: 

A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
dados = {}
ficha = list()
resp = ''
soma_das_idades = media = 0


while True:
    dados['nome'] = str(input('Nome: '))

    while True:
        sexo = str(input('Digite o Sexo: M ou F: '))
        if sexo in 'Mm' or sexo in 'Ff':
            dados['sexo'] = (sexo)
            break
        else:
            print('Erro! digite apenas M ou F')

    dados['idade'] = int(input('Digite a idade: '))

    ficha.append(dados.copy())

    resp = str(input('Quer continuar? S/N '))
    print('-='*30)
    while resp not in 'SsNn':
        print('Erro digite apenas S ou N!')
        print('-='*30)
        resp = str(input('Quer continuar? S/N '))

    if resp in 'Nn':
        break


print('-='*30)
print(f'No total foram {len(ficha)} Cadastradas.')

for v in ficha:
    for k, v in v.items():
        if k == 'idade':
            soma_das_idades += v

media = (soma_das_idades / len(ficha))

print(f'A media das idades é {media}')


print('As mulheres cadastradas são: ', end=' ')

for v in ficha:
    for k, i in v.items():
        if k == 'sexo' and i in 'Ff':
            print(f'{v["nome"]}', end=', ')

print('')

print('D) Lista das pessoas a cima da media')
for v in ficha:
    if v['idade'] >= media:
        print(f'   ====>> nome = {v["nome"]},  sexo = {v["sexo"]},  idade = {v["idade"]}')
