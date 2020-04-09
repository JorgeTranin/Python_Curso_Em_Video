'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários
  valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
  ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
  em ordem crescente.'''

lista = list()
c = 0
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Esse numero já se encontra na lista digite outro ou saia: ')
    v = str(input('Quer continuar?[S/N] '))
    if v in 'Nn':
        break

lista.sort()

print(lista)

    