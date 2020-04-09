#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#  cosseno e tangente desse ângulo
from math import tan, cos, sin, radians
a = float(input('Digite o angulo: '))
r = radians(a)
se = sin(r)
co = cos(r)
ta = tan(r)

print('O calculo do seno é {:.2f}\nO do coseno é {:.2f}\nE a tangente é {:.2f}'.format(se, co, ta))