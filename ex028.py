import random
from time import sleep
print('-=-'*20)
num = int(input('Vou pensar em um número entre 0 e 5, tente advinhar:  '))
print('-=-'*20)
lista = [0,1,2,3,4,5]
print('AGUARDE PROCESSANDO...')
sleep(3)
escolhido = random.choice(lista)

if escolhido == num:
    print('Eu escolhi o número {} Parabéns! Você ganhou!'.format(escolhido))
else:
    print('Você perdeu! Eu escolhi o número {}'.format(escolhido))
    print('**********FIM DO PROGRAMA****************')