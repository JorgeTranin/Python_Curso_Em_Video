'''
Exercício Python 080: Crie um programa onde o usuário possa digitar
cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista
ordenada na tela.
'''

lista = list()

for i in range(0, 4):
    n = int(input('Digite um valor: '))

    if i == 0:
        lista.append(n)
        print('Valor adicionado no inicio da lista')
    
    elif n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no final da lista!')

    else:
        posiçao = 0
        while posiçao < len(lista):
            if n <= lista[posiçao]:
                lista.insert(posiçao, n)
                print(f'Adicionei na posição {posiçao}ª')
                break
            posiçao +=1

print(f'Os valores digitados em ordem são:{lista}')
            



   
    
    