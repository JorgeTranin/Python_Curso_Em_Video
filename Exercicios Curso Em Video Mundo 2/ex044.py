preço = float(input('Digite o preço do produto R$'))
print('''Como irá pagar? 
[1] A vista no dinheiro
[2] A vista no cartao
[3] Até 2X no cartao
[4] 3x ou mais no cartao''')
opção = int(input('Qual opção? '))
if opção == 1:
    print('O produto de custava R${} custara R${}.'.format(preço, preço-(preço*10/100)))
elif opção == 2:
    print('O produto de custava R${} custara R${}.'.format(preço, preço-(preço*5/100)))
elif opção == 3:
    print('2x no cartao custara R${}.'.format(preço))
elif opção == 4:
    print('O produto de custava R${} custara R${}.'.format(preço, preço+(preço*20/100)))
