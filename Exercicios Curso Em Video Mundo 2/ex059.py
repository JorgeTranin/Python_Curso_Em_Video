n = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
s = 1
while s != 5:

    print('''
    [1] somar
    [2] Multiplicar
    [3] maior numero
    [4] Novos numeros
    [5] Sair do programa''')
    s = int(input('Qual opçao?'))
    if s == 1:
        print('A soma entre {} e {} = {}'.format(n, n2, n+n2))
    elif s == 2:
        print('A multiplicação de {} e {} = {}'.format(n, n2, n*n2))
    elif s == 3:
        if n > n2:
            print('O maior numero entre {} e {} é {}'.format(n, n2, n))
        else:
            print('O maior numero entre {} e {} é {}'.format(n, n2, n2))
    elif s == 4:
        print('Quai são os novos numeros? ')
        n = int(input('digite um numero: '))
        n2 = int(input('Digite outro valor: '))
print('Obrigado')