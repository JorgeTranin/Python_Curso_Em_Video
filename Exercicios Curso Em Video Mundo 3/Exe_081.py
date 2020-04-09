'''
Exercício Python 081: Crie um programa que vai ler vários
números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.

'''

lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))

    n = str(input('Quer continuar? S/N: '))

    if n in 'Nn':
        break


lista.sort(reverse=True)
print(f'Voce digitou {len(lista)} Valores.')

print(f'Os valores em ordem decrecente são:{lista}')

if  lista.count(5) == 0:
     print('O valor 5 não esta na lista')
else:
    print('O valor 5 foi digitado e esta na lista')

