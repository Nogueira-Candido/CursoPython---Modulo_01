peso = float(input('Digite o seu peso (KG): '))
altura = float(input('Digite a sua altura (M): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('O seu IMC é {:.1f}. Você está ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc <= 24.9:
    print('O seu IMC é {:.1f}. Você possui o PESO IDEAL.'.format(imc))
elif imc >25 and imc <=29.9:
    print('O seu IMC é {:.1f}. Você está com SOBREPESO'.format(imc))
elif imc >30 and imc <=39.9:
    print('O seu IMC é {:.1f}. Você está OBESO.'.format(imc))
else:
    print('Você possui OBESIDADE MORBIDA.')