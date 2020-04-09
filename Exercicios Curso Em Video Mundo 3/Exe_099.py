def maior(lista):
    
    print(f'Foram passados um total de {len(lista)} valores')
    m = 0
    for v in lista:
        if v > m:
            m = v
    print(f'O maior valor informado foi {m}')


maiores = list()
while True:
    maiores.append(int(input('Digite um numero: ')))

    resp = str(input('Quer continuar? S/N ')).upper()
    if resp in 'N':
        break

print(maiores)

maior(maiores)
