lista = []
for c in range(1,6):
    lista.append(float(input('Digite o peso da {}ª pessoa: '.format(c))))
print('O maior peso foi de {:.2f}kg'.format(max(lista)))
print('O menor peso foi  de {:.2f}kg'.format(min(lista)))
