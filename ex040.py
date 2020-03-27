n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média foi {:.2f} portanto, você foi REPROVADO.'.format(media))
elif media > 5.0 and media <= 6.9:
    print('Sua média foi {:.2f} portanto, você está em RECUPERAÇÃO.'.format(media))
else:
    print('Média igua a {:.2f}, parabéns você foi APROVADO.'.format(media))