vel = int(input('Digite a velocidade do carro: '))
ultrapassagem = vel - 80
multa = ultrapassagem * 7

if(vel > 80):
    print('Você ultrapassou o limite de velocidade que é 80km/h')
    print('\033[7:33mValor da multa:\033[m \033[31m RS{:.2f}'.format(multa))
else:
    print('\033[1:36:40mVelocidade permitida {} Km/h\033[m'.format(vel))