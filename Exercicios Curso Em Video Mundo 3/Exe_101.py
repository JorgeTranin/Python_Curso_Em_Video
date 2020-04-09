'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO,
OPCIONAL e OBRIGATÓRIO nas eleições.

'''


def voto(idade):
    """[Funções para votação]

    Arguments:
        idade {[int]} -- [informa a idade no ano atual da pessoa]

    Returns:
        [str] -- [Retorna se a pessoa pode votar ou não]
    """

    from datetime import date
    n = date.today().year - idade
    if n <= 15:
        return print(f'Com a idade de {n} você não pode votar ainda')
    elif 16 <= n < 18 or n > 65:
        return print(f'Com a idade de {n} Voto opcional')

    else:
        return print(f' Com a idade de {n} Voto obrigatorio')


idade = int(input('Digite o ano que vc nasceu: '))

voto(idade)
