soma = 0
cout = 0

for c in range(1, 501, 2):

    if c % 3 == 0:
        cout += 1
        soma += c

print('A soma de {} números é igual a {}'.format(cout,soma))