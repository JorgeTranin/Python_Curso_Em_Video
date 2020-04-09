cont = 1
while True:
    t = int(input('Quer saber a tabuada de que numero ? '))
    if t < 0:
        break
    for c in range (1, 11):
        print(f'{t} X {c} = {t * c}')
print('Obrigado!')