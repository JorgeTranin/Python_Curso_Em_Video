cont = 0
m18 = H = F = 0

while True:
    cont += 1
    s = ' '
    id = int(input('idade: '))
    while s != 'M' and s != 'F':
        s = str(input(f' pessoa: M/ F: ')).upper().strip()[0]
    print('-=-' * 20)
    c = str(input('Quer cadastrar mais alguem? [S/N]: ')).upper().strip()[0]
    if id >= 18:
        m18 += 1
    if s == 'M':
        H += 1
    if s == 'F' and id < 20:
        F += 1
    if c == 'N':
        break
print('-=-'*20)
print(f' Tem {m18} Pessoas acima de 18 anos')
print(f' {H} Homens foram cadastrados.')
print(f' {F} Mulheres tem menos de 20 anos.')