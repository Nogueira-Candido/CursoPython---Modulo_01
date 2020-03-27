import random
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1,-1,-1):
    inverso +=junto[letra]
print('A frase digitada é {} o seu inverso é {}'.format(junto,inverso))
if junto == inverso:
    print('A frase digitada é um palídromo.')
else:
    print('A frase digitada não é um Palídromo.')