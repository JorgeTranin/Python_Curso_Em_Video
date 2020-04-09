from random import randint
from time import sleep
numeros = list()

def sorteia():
    for i in range(0, 5):
        s = randint(1, 100)
        numeros.append(s)

def somaPar():
    soma = 0
    for i, v in enumerate(numeros):
        soma += v
        

sorteia()

somaPar()
print(numeros)
print(soma)

