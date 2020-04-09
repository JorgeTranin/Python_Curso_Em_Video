from datetime import date
i = int(input('Digite o ano de seu nascimento! '))
ano =  date.today().year - i

if ano < 18:
    print('Você ainda nao precisa se alistar faltam {} anos'.format(18-ano))
elif ano == 18:
    print('Esta na hora de se alistar')
elif ano > 18:
    print('Você passou {} anos da hora de se alistar'.format(ano-18))
