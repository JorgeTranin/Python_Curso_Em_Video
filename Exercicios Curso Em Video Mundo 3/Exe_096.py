def area(): 
    
    print(f'A área do terreno {l :.1f} X {c :.1f} é {l*c :.2f} M²')


#! Programa principal

print('       Controle de terrenos')
print('-'*30)

l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))

area(l, c)
