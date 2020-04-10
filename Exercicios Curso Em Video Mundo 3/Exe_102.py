def fatorial(n, show=False):
    """[Calculo do fatorial de um número]

    Arguments:
        n {[int]} -- [Numero a ser calculado o fatorial]
    """
    if n == 0:
        n = 1
    f = 1
    cont = n
    while cont != 1:
        
        if show:
            print(f'{cont} X ', end='')
        f *= cont
        cont -= 1
    return f


print(f'= {fatorial(5)}')
