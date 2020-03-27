num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('O primeiro valor digitado ({}) é maior do que o segundo valor digitado ({})'.format(num1,num2))
elif num1 < num2:
    print('O segundo valor digitado ({}) é maior do que o primeiro valor digitado ({})'.format(num2,num1))
else:
    print('Não existe valor maior ({}) e ({}) são iguais'.format(num1,num2))