import random
idade = 0
soma = 0
maiorIdadeHomem = 0
nomeVelho = ''
for c in range(1,5):
    print('-------- {}ª Pessoa -------'.format(c))
    nome = str(input('DIGITE UM NOME:'))
    idade = int(input('DIGITE A IDADE : '))
    sexo = input('DIGITE O SEXO [F/M]: ')
    soma += idade
    media = soma / 4
    if c == 1 and  sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome

print('MEDIA DAS IDADE DO GRUPO: {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem,nomeVelho))