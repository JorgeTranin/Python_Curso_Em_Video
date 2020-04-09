n1 = float(input('Digite a sua primeira nota! '))
n2 = float(input('Digite a sua segunda nota! '))

m = (n1 + n2)/2
if m < 5:
    print('Com a nota {} você reprovou.'.format(m))
elif m <=6.9 and 5:
    print('Com nota {} vc esta de recuperação.'.format(m))
elif m >= 7:
    print('Com nota {} voce foi aprovado.'.format(m))
