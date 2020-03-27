a = float(input('Digite a medida A do triângulo: '))
b = float(input('Digite a medida B do triângulo: '))
c = float(input('Digite a medida C do triângulo: '))


if (b - c < a and a < b + c) and (a - c < b and b < a + c) and (a - b < c and c < a + b):
    print( 'Medidas informadas formam um triângulo ', end='')
    if (a == b) and (a == c) and (b == c):
        print('EQUILATERO')
    elif (a == b) or (a == c) or (b == c):
        print('ISOCELES')
    elif (a != b) and (a != c) and (b != c):
        print('ESCALENO.')
else:
    print('As medidas informadas não formam um triângulo.')