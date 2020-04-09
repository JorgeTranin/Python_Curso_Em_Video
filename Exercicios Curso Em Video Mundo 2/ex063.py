print('='*20)
print('Sequencia de Fibonacci')
print('='*20)
n = int(input('Digite quantos termos vc quer mostrar: '))
t = 0
t1 = 1
c = 3
print('{} -> {}'.format(t, t1), end=' -> ')
while c <= n :
    t2 = t + t1
    print('{}'.format(t2),end=' -> ')
    t = t1
    t1 = t2
    c = c + 1
print('FIM.')