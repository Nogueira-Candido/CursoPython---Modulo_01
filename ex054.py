from datetime import date
cout = 0
cout1 = 0
for c in range(1,8):
    ano = int(input('{} - Digito seu ano de nascimento: '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        cout +=1
    else:
        cout1+=1
print('{} pessoas atingiram a maior idade penal.'.format(cout))
print('{} pessoas não atingiram a maior idade penal.'.format(cout1))