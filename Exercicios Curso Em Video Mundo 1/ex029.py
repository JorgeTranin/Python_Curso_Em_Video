v = int(input('Digite a velocidade do carro: '))
m = (v - 80)*7

if v > 80:
    print('Você foi multado ultrapassou o limite de 80 KM/H')
    print('A multa a ser paga é de {}R$.'.format(m))
else:
    print('Não ajudou na fabrica de multa, vai embora! ')