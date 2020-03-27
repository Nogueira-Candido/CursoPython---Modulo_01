n = int(input('Digite um número que você deseja saber a tabuada: '))
op = int(input(
    '''
    ESCOLHA A OPERAÇÃO DESEJADA:
    [ 0 ] - ADIÇÃO
    [ 1 ] - SUBTRAÇÃO
    [ 2 ] - MULTIPLICAÇÃO
    [ 3 ] - DIVISÃO
    
    '''
))
print('\nTABUADA DE {}\n'.format(n))
for c in range(1,11):
    if op == 0:
        t = n+c
        print('{} + {} = {} '.format(n, c, t))
    elif op == 1:
        t = n-c
        print('{} - {} = {} '.format(n, c, t))
    elif op == 2:
        t = n*c
        print('{} x {} = {} '.format(n, c, t))
    elif op == 3:
        t = n/c
        print('{} / {} = {:.2} '.format(n, c, t))
    else:
        print('OPÇÃO INVÁLIDA!')
print('{:=^15}'.format(''))