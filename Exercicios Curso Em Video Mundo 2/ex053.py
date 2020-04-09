frase = str(input('Digite uma frase: ')).strip().upper()
pa = frase.split()
junto = ''.join(pa)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('A frase é um palindromo.')
else:
    print('A frase não é um palindromo.')
