soma = 0
tot2 = barato = cont =  0
nov = ' '
while True :
    n = str(input('Nome do produto: '))
    p = float(input('Preço: '))
    soma += p
    c = ''
    cont += 1
    while c != 'S' and c != 'N':
        c = str(input('Quer cadastrar mais algum? [S/ N]: ')).upper().strip()[0]
    if cont == 1:
        barato = p
        nov = n
    if p >= 1000:
        tot2 += 1
    if p < barato:
        barato = p
        nov = n
    if c == 'N':
        break
print('-=-'*20)
print(f'Total gasto na compra R${soma:.2f}')
print(f'{tot2} produtos que custam acima de 1000 R$')
print(f'O nome do produto mais barato é {nov} e custa R${barato}')
