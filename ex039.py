from datetime import date
anoNasc = int(input('Digite o seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
tempoFalta = 18 - idade
tempoPassou = (anoAtual - 18) - anoNasc
anoAlistamento1 = anoAtual - tempoPassou
anoAlistamento2 = anoAtual + tempoFalta
print('Idade {} anos.'.format(idade))

if idade < 18:
    print('Você ainda não possui idade para o alistamento.')
    print('Tempo que resta: {} ano(os).'.format(tempoFalta))
    print('O seu alistamento será em {}'.format(anoAlistamento2))
elif idade == 18:
    print('Atenção! É hora de realizar o alistamento.')
elif idade > 18:
    print('Você já passou do prazo para o alistamento. Procure o serviço militar.')
    print('Tempo que passou: {} ano(os).'.format(tempoPassou))
    print('O seu alistamento foi no ano de {}'.format(anoAlistamento1))


