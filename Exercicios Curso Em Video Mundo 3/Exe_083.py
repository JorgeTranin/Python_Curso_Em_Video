'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com
os parênteses abertos e fechados na ordem correta.

'''

lista_Parenteses = []
c1 = 0
c2 = 0
exp= str(input('Digite a expressão: '))

for i in exp:
    if i == '(':        
        lista_Parenteses.append(i)
        
    elif i == ')':
        lista_Parenteses.append(i)
        
for i in lista_Parenteses:
    

print(lista_Parenteses )



