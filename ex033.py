cores = {'limpa':'\033[m',
         'roxo':'\033[35m',
         'vermelho':'\033[31m'
        }
n1 = int(input('DIGITE O PRIMEIRO NÚMERO: '))
n2 = int(input('DIGITE O SEGUNDO NÚMERO: '))
n3 = int(input('DIGITE O TERCEIRO NÚMERO: '))

#VERIFICANDO O MENOR NÚMERO
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('{}{} É O MENOR NÚMERO DIGITADO{}'.format(cores['roxo'], menor, cores['limpa']))

#VERIFICANDO O MAIOR NÚMERO
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('{}{} É O MAOIR NÚMERO DIGITADO.{}'.format(cores['vermelho'], maior, cores['limpa']))



'''
#VERIFICANDO SE O PRIMEIRO NÚMERO É MAIOR
if n1 > n2 and n1 > n3:
    print('O PRIMEIRO NÚMERO DIGITADO É O MAIOR: ')

#VERIFICANDO SE O PRIMEIRO NÚMERO É O MENOR
if n1 < n2 and n1 < n3:
    print('O PRIMEIRO NÚMERO DIGITADO É O MENOR ')

#VERIFICANDO SE O SEGUNDO NÚMERO É O MAIOR
if n2 > n1 and n2 > n3:
    print('O SEGUNDO NÚMERO DIGITADO É O MAIOR')

#VERIFICANDO SE O SEGUNDO NÚMERO DIGITADO É O MENOR
if n2 < n1 and n2 < n3:
    print('O SEGUNDO NÚMERO DIGITADO É O MENOR')

#VERIFICANDO SE O TERCEIRO NÚMERO DIGITADO É O MAIOR
if n3 > n1 and n3 > n2:
    print('O TERCEIRO NÚMERO DIGITADO É O MAIOR')

#VERIFICANDO SE O TERCEIRO NÚMERO DIGITADO É O MENOR
if n3 < n1 and n3 < n1:
    print('O TERCEIRO NÚMERO É O MENOR')
'''

