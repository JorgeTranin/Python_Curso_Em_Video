s = float(input('Digite seu salario: '))

if s > 1250:
    print('O almento em seu salario é de {}'.format(s * 10 / 100))
    print('Seu novo salario é de {}'.format(s * 10 / 100 + s))

else:
    print('O almento no seu salario é de {}'.format(s*15/100))
    print('Seu novo salario é de {}'.format(s * 15 / 100 + s))
