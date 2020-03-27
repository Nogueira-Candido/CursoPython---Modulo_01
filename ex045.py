import random
print('{:=^40}'.format(' JOKENPÔ '))
print('''
ESCOLHA DENTRE AS OPÇÕES:
[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA
''')
voce = int(input('QUAL A OPÇÃO VOCÊ ESCOLHE? '))

lista = ['PEDRA','PAPEL','TESOURA']


maquina = random.choice(lista)


print('A MÁQUINA ESCOLHEU:{}'.format(maquina))

if voce == 1 and maquina == 'TESOURA':
    print('VOCÊ GANHOU!')
elif voce == 3 and maquina == 'PAPEL':
    print('VOCÊ GANHOU!')
elif voce == 2 and maquina == 'PEDRA':
    print('VOCÊ GANHOU!')
elif voce == 1 and maquina == 'PEDRA' or voce == 2 and maquina == 'PAPEL' or voce == 3 and maquina == 'TESOURA':
    print('JOGO EMPATADO!')
else:
    print('MAQUINA GANHOU!')

