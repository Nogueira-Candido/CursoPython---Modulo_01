nomeCompleto = str(input('Digite o seu nome completo ')).strip() #elimina os espaços caso o cliente coloque ao digitar

nomeCompleto.split() #separa os nomes

print('Seu primeiro nome é: ', nomeCompleto.split()[0])
print('Seu ultimo nome é: ', nomeCompleto.split()[-1])