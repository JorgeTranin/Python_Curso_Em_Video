casa = float(input('Qual o valor da casa? '))
s = float(input('Quanto voce ganha? '))
ano = int(input('Quantos anos irá pagar? '))

ex = (s * 30/100)
p = casa/(ano*12)

if p <= ex:

    print('Voc pode comprar essa casa! ')
    print('O valor da parcela vai custar R${:.2f}'.format(p))
else:
    print('Voce nao pode pegar o emprestimo')
