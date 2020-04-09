from time import sleep
s = 1
while s != 'M' and s != 'F' :
    s = str(input('Digite seu sexo [M/F]: ')).upper()
    sleep(2)
    if s != 'M' and s != 'F':
        print('Digite novamente! ')
print('Parabens!')

