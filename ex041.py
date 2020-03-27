from datetime import date
anoNasc = int(input('Digite o ano de nascimento do atleta: '))

idade = date.today().year - anoNasc

if idade <= 9:
    print('Idade {} anos - categoria = MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Idade {} anos - categoria  = INFANTIL.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Idade {} anos - categoria = JUNIOR.'.format(idade))
elif idade > 19 and idade <=20:
    print('Idade {} anos - categoria = SÊNIOR'.format(idade))
else:
    print('Idade {} anos - categoria = MASTER.'.format(idade))