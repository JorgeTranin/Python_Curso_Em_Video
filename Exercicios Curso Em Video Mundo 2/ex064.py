
c = 0
cont = 0
soma = 0
while c != 999:
    c = int(input('Digite um valor [999 para parar ]: '))
    soma = c + soma
    cont +=  1
print('FIM')
print('Foram digitados {} numeros e a soma de todos é {}'.format((cont - 1),(soma - 999)))