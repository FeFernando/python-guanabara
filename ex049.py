num = int(input('Digite o numero que você quer a tabuada: '))
for c in range(1, 11):
    res = num * c
    print('{} x {} = {}'.format(num, c, res))