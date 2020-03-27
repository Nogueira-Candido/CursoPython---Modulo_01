distancia = int(input('Qual a distancia percorrida? '))

preçoPassagem1 = distancia * 0.50
preçoPassagem2 = distancia * 0.45

if distancia < 200:
    print('Vocẽ percorreu {} km/h, portanto o preço da passagem será R${:.2f} '.format(distancia,preçoPassagem1))
if distancia > 200:
    print('Você percorreu {} km/h, portanto o preço da passagem será R${:.2f}'.format(distancia,preçoPassagem2))