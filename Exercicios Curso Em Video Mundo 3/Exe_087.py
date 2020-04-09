'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.

'''

matriz = [ [], [], [] ]
somapares = somaterceira = maiorsegundalinha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para a posição [{l} {c}] ')))

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()

for l in range(0, 3):
    for c in range( 0,3):
        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        if c == 2 :
            somaterceira += matriz[l][c] 

for l in range(0,3):
    if l == 1:
        if matriz[l][c] > maiorsegundalinha:
            maiorsegundalinha += matriz[l][c]
print(f'A soma dos numeros pares é de {somapares}')
print(f'A soma da terceira coluna é {somaterceira}')
print(f'O maior valor da segunda linha é {maiorsegundalinha}')