
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}

n1 = int(input('Digite N1: '))
n2 = int(input('Digite N2: '))
s = int(n1+n2)
print('A soma de {}{}{} e {}{}{} vale {}{}{} '.format(cores['azul'],n1,cores['limpa'], cores['amarelo'],n2,cores['limpa'],cores['pretoebranco'],s,cores['limpa']))