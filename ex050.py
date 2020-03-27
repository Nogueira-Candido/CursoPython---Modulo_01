soma = 0
for n in range(1,7):
    n = int(input('Digite o {}º número: '.format(n)))
    if n %2 == 0:
        soma += n
print('A soma dos números pares digitados é igual a: {}'.format(soma))
