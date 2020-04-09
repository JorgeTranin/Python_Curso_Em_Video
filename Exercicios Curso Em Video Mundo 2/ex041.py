from datetime import date
n = int(input('Digite o ano que voce nasceu: '))
ano = date.today().year - n
if ano <=9:
    print('Com a idade de {} Categoria MIRIM'.format(ano))
elif ano <=14 and 9:
    print('Com a idade {} Categoria INFANTIL'.format(ano))
elif ano <= 19 and 14:
    print('Com a idade {} categoria JUNIOR'.format(ano))
elif ano <=20 and 19:
    print('Com a indade {} Categoria SENIOR'.format(ano))
elif ano >21:
    print('Com a idade {} categoria MASTER'.format(ano))