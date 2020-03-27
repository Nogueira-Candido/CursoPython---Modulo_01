''' Para construir um triângulo é necessário que a
medida de qualquer um dos lados seja menor que a soma
das medidas dos outros dois e maior que o valor absoluto
da diferença entre essas medidas.
'''

a = float(input('Digite a medida A do triângulo: '))
b = float(input('Digite a medida B do triângulo: '))
c = float(input('Digite a medida C do triângulo: '))

if (b - c < a and a < b + c) and (a - c < b and b < a + c) and (a - b < c and c < a + b):
    print( 'Medidas informadas formam um triângulo.')
else:
    print('As medidas informadas não formam um triângulo.')