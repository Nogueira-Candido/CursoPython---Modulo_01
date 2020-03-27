frase = str(input('Digite uma frase qualquer: '))

print('Quantas vezes aparece a letra A? {} vezes'.format( frase.count('A')))
print('Em que posição a letra A aparece a primeira vez? Na posição de nº {} '.format(frase.find('A')))
print('Em que posição a letra A aparece a última vez? Na posição de nº {}'.format(frase.rfind('A')-1))