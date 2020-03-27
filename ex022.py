cores = {'limpa':'\033[m',
        'negvermelho':'\033[7:31m'}



nomeCompleto = str(input('DIGITE O SEU NOME COMPLETO: '))
print(nomeCompleto.upper())
print(cores['negvermelho'],nomeCompleto.lower(), cores['limpa'])
print('Quantidade de Letras sem consideras os espaços: ', len(''.join(nomeCompleto.split())))
print('Quantas letras tem o primeiro nome: ', len(nomeCompleto.split()[0]))