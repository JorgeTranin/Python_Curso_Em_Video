from time import sleep

def contador(ini, f, p):
    """[O programa gera uma contagem]
    
    Arguments:
        ini {[int]} -- [inicio da contagem]
        f {[int]} -- [fim da contagem]
        p {[int]} -- [passo da contagem]
    """
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-'*30)
    print(f'Contando de {ini} até {f} pulando de {p} em {p}')
    sleep(1.5)
    if ini < f:
        for i in range(ini -1, f, p):
            sleep(0.5)
            print(i+1, end=' ', flush=True)
        print('FIM')

    else:
        for i in range(ini -1, f -2, - p):
            print(i+1, end=' ', flush=True)
            sleep(0.5)

        print('FIM')
    print('-'*30)

#programa principal!

contador(1, 10, 1)
contador(10, 0, 2)

print('Sua vez, quer contar de quanto a quanto? ')

ini = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite de quanto e quanto quer pular: '))

contador(ini, f, p)

help(contador)