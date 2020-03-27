cores = {'limpa':'\033[m',
         'amarelo ':'\033[33m',
         'margenta':'\033[34m',
         'roxo':'\033[35m'}

num = int(input('Digite um número: '))
opcao = int(input('''Escolha a opção de conversão: 
[1] - Binário [2] - Octal [3] - Hexadecimal: '''))
if opcao == 1:
    print('O número {} em binário é igual a {} {}{}'.format(num,cores['amarelo '],bin(num)[2:],cores['limpa']))
elif opcao == 2:
    print('O número {}{}{} em Octal é igual a {}{}{}'.format(cores['amarelo '],num,cores['limpa'], cores['margenta'], oct(num)[2:], cores['limpa']))
elif opcao == 3:
    print('O número {} em hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Digite um número entre 1 e 3')
