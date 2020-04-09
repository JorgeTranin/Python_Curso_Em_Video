'''
Exercício Python 082: Crie um programa que vai ler vários números
e colocar em uma lista. Depois disso, crie duas listas extras que
vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.

'''

lista_total = []
lista_Pares = []
lista_Impares = []

print('-='*30)

while True:
    lista_total.append(int(input('Digite um valor: ')))

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

for v in lista_total:
    if v %2 == 0:
        lista_Pares.append(v)
    else:
        lista_Impares.append(v)
print('-='*30)
print(f'A lista total é: {lista_total}')
lista_Impares.sort()
lista_Pares.sort()
print('-='*30)
print(f'Os pares são {lista_Pares}')
print('-='*30)
print(f'Os impares são {lista_Impares}')
print('-='*30)