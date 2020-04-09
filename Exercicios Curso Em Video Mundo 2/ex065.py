r = ''
cont = soma = maior = 0

while r != 'N':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar ? [S/N]')).strip().upper()
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
med = soma / cont
print('Voce digitou {} numeros e a media dos valore é de {:.2f}'.format(cont ,med))
print('O maior valor foi {} e o menor {}'.format(maior, menor))
print(f'a soma é {soma}')