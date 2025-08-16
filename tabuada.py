num = int(input('Digite um numero para saber sua tabuada'))
print('_' * 12)
for c in range (0, 11):
    res = num * c
    print('{} x {} = {}'.format(num, c, res))
print('_' * 12)