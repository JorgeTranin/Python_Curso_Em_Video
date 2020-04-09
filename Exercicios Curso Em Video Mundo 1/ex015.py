#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km voce rodou com o carro? '))
d = float(input('Quantos dias vc ficou com o carro? '))
preço = (km * 0.15) + (d * 60)

print('Com {} dias e {} Km rodados, O preço a pagar pelo aluguel é de R${}'. format(d, km, preço))