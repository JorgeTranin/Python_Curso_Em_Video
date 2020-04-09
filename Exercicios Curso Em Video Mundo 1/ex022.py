#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas;
#– Quantas letras ao todo (sem considerar espaços);
#– Quantas letras tem o primeiro nome.

n = str(input('Digite seu nome! ')).strip()
frase = n
div = frase.split()
#div2 = div[0]
print('Seu nome com todas as letras maiusculas {}'.format(frase.upper()))
print('Seu nome com todas as letras minusculas {}'.format(frase.lower()))
print('Total de letras sem espaço é: ', (len(frase) - frase.count(' ')))
print('O total de letras no primeiro nome é: ', (len(div[0])))

