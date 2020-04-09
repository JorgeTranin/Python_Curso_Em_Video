soma = 0
mulhres = 0
maisvelho = 0
nomehomem = ''
for c in range(1, 5):
    print('--------{}ºpessoa-------'.format(c))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]')).strip().upper()
    soma = soma + idade
    print('{}\n{}\n{}\n'.format(nome, idade, sexo))

    if c == 1 and sexo in 'Mm':
        maisvelho = idade
        nomehomem = nome

    if sexo in 'Mm' and idade > maisvelho:
        maisvelho  = idade
        nomehomem = nome

    if idade <= 20 and sexo in 'Ff':
        mulhres += 1

print('A media de Idade do grupo é {:.1f}'.format(soma/4))
print('O total de mulheres com menos de 20 anos é de {}'.format(mulhres))
print('O homem mais velho tem {} anos e se chama {}'.format( maisvelho, nomehomem))
