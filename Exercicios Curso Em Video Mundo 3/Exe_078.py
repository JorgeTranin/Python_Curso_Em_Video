lista = list()

for i in range(0, 4):
    lista.append(int(input(f'Digite um valor para a posição {i}º:')))


print(f'Voce digitou os numeros: {lista}')

print(f'O maior valor é {max(lista)} e sua posição na lista é :', end=' ')
maior = max(lista)
for i, v in enumerate(lista):
    if lista[i] == maior:
        print(i, end='...')
print(' ')
print(f'O menor valor é {min(lista)} e sua posição na lista é ',end=' ')
menor = min(lista)
for i, v in enumerate(lista):
    if lista[i] == menor:
        print(i, end='...')