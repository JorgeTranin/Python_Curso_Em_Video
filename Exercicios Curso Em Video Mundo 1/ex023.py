#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e
#  mostre na tela cada um dos dígitos separados.

n = int((input('Digite um numero! ')))

print('Unidade:', (n[3]))
print('Dezena:', (n[2]))
print('Centena:',(n[1]))
print('Milhar:', (n[0]))

