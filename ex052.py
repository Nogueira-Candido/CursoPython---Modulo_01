num = int(input('DIGITE UM NÚMERO: '))
tot = 0
for c in range(1, num + 1):
    if num % c==0:
         print('\033[33m', end='')
         tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\nO número {} foi dividido {} vezes'.format(num,tot, end=''))
if tot  == 2:
    print('Portanto, O número {}  é PRIMO.'.format(num, end=''))
else:
    print('Portanto, O número {} não é PRIMO.'.format(num) )