from datetime import date
soma = 0
soma2 = 0
for c in range(1, 8):
    p = int(input('Digite o ano de seu nascimento da {}º pessoa:'.format(c)))
    ano =  date.today().year - p
    if ano <= 21:
        soma = soma + 1
    else:
        soma2 = soma2 + 1
print('O total de pessoa menores de idade é {}'.format(soma))
print('O total de pessoas maiores de idade é {}'.format(soma2))
