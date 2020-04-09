a = int(input('Digite um numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

print('Analisando os numeros {}, {} e {}'.format(a, b, c))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor é {}'.format(menor))
print(('O maior é {}'.format(maior)))