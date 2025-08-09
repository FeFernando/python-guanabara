num = int(input('Digite um numero para saber se ele é primo: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
if tot == 2 :
    print('Esse numero  é primo')
else:
    print('Esse numero não é primo')