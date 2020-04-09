'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

'''

principal = list()


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    
    media = (nota1 + nota2) / 2
    
    principal.append([nome, nota1, nota2, media])

    resp = str(input('Quer continuar? S/N: '))

    if resp in 'Nn':
        break

    

print('Nº     Nome      Media')
print('-='*30)
for v in range(0, len(principal)):
    print(f'{v}      {principal[0][0]}        {principal[0][3]}')
    
    

while True:
    resp = int(input('Quer mostrar a nota de qual aluno? [999] para interromper: '))

    if resp == 999:
        break
    elif resp not in range(0, len(principal)):
        print('Aluno não esta na lista! tente de novo')
    else:
        print(f'O aluno: {principal[resp][0]} Tem as notas [{principal[resp][1]}, {principal[resp][2]}]')
        
        
