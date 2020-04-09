r = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da primeira reta: '))
r3 = float(input('Digite o tamanho da primeira reta: '))

if r < r2+r3 and r2 < r + r3 and r3 < r + r2:

    print('Com essas retas vc consegue formar um triangulo: ')

else:
    print('Isso nao forma um triangulo')