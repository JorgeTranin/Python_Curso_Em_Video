'''Exercício Python 075: Desenvolva um programa que leia
 quatro valores pelo teclado e guarde-os em uma tupla.
  No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''


num = (int(input(('Digite um valor: '))), int(input(('Digite um valor: '))),
int(input(('Digite um valor: '))), int(input(('Digite um valor: '))) )
   
print(num)
print(num.count(9))
print(f'O valor 3 apareceu na {num.index(3)}ª posição.')
print('Os valores pares são ',end=' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')