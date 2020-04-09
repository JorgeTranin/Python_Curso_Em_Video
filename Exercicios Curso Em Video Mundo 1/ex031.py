v = float(input('Digite a distancia da viagem: '))

if v <= 200:
    p = v * 0.50
else:
    p = v * 0.45

print('A passagem vai custar {}R$'.format(p))
print('-'*20, 'Boa viagem', '-'*20)