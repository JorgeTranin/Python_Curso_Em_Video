'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete
valores numéricos e cadastre-os em uma lista única que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e ímpares
em ordem crescente.

'''

principal = [[], []]

for i in range(0, 6):
    aux = int(input('Digite um valor: '))

    if aux % 2 == 0:
        principal[0].append(aux)
        
    else:
        principal[1].append(aux)
    

principal[0].sort()
principal[1].sort()

print(f'Os valores pares são {principal[0]}')
print(f'Os valores pares são {principal[1]}')

    



    

