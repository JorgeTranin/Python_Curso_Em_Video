p = float(input('Digite o preço do produto: R$'))
n = p - (p * 5 / 100)

print('O preço que custava R${} agora esta por R${}'.format(p, n))