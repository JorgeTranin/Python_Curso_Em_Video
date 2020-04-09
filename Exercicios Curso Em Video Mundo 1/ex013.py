s = float(input('Digite seu salario: R$'))
a = s + (s * 15 / 100)

print('Você recebe R${:.2f}\nVC passa a receber com 15% de aumento R${:.2f}'.format(s, a))