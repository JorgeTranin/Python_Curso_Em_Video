n1 = int(input('Digite um numero! '))
n2 = int(input('Digite outro numero! '))

if n1 > n2:
    print('Entre {} e {} O primeiro valor é maior'.format(n1, n2))
elif n2 > n1:
    print('Entre {} e {} O segundo valor é maior.'.format(n1, n2))
elif n1 == n2:
    print('Os dois valores são iguais.')

