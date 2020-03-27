media = 0
soma = 0
maiorIdadeHomem = 0
nomeVelho = ''
for c in range(1,5):
    print('-------- {}ª Pessoa -------'.format(c))
    nome = str(input('DIGITE UM NOME:')).strip()
    idade = int(input('DIGITE A IDADE : '))
    sexo = input('DIGITE O SEXO [F/M]: ').strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome

media = soma / 4
print('MEDIA DAS IDADE DO GRUPO: {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem,nomeVelho))