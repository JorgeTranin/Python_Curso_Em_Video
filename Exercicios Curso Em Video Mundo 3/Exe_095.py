'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione
com vários jogadores, incluindo um sistema de visualização de
detalhes do aproveitamento de cada jogador.

'''

ficha = {}
gols = []
time = list()
while True:
    ficha['nome'] = str(input('Digite o nome do jogador: '))

    resp = int(input(f'Quantas partidas {ficha["nome"]} jogou: '))
    print('-='*30)
    for i in range(0, resp):
        gols.append(int(input(f'       Quantos gols na partida {i+1}: ')))

    soma = 0
    for n in gols:
        soma += n

    ficha['gols'] = gols[:]
    ficha['aproveitamento'] = soma
    time.append(ficha.copy())

    r = str(input('Quer continuar? ')).upper()[0]
    if r == 'N':
        break
print('-='*40)
print(ficha)
print('-='*40)

print('cod   Nome            gols             total ')
for i, v in enumerate(time):
    print(f'  {i :<1} {v["nome"] }  {v["gols"] }      {v["aproveitamento"] :>5}')