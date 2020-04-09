'''Exercício Python 077: Crie um programa que tenha uma tupla com várias
  palavras (não usar acentos). Depois disso, você deve mostrar, para cada
  palavra, quais são as suas vogais.'''

palavrass = ('Jogos',' treino','futebol','coronavirus')

for palavra in palavrass:
    print(' ')
    print(f'Na palavra {palavra.upper()} tem as vogais: ',end=' ')
    for letra in palavra:
        if letra in 'aeiou':
          print(f'{letra}', end=' ')