tabu = int(input('Digite um numero para saber sua tabuada: '))
print('-='*10)
for b in range(1, 11):
     print('{} x {} = {}'.format(tabu, b, tabu*b))
print('-='*10)