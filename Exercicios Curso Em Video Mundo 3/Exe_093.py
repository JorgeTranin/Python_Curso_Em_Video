'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols
feitos durante o campeonato.

'''
ficha = {}
gols = []
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

print('-='*40)
print(ficha)
print('-='*40)
for k, v in ficha.items():
    print(f'O campo {k} tem {v}')
print('-='*40)

print(f'O jogador {ficha["nome"]} jogou {len(ficha["gols"])} partidas')

for i, v in enumerate(ficha['gols']):
    print(f'   ++> no jogo {i+1} fez {v} Gols')

print(f'O aproveitamento foi de {ficha["aproveitamento"]}')
    





    