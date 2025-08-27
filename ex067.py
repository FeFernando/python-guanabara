n = 0
res = 0
while True:
    n = int(input('Digite um numero e mostrarei a tabuada dele: '))
    if n < 0:
        break
    for c in range (1, 11):
        res = n * c
        print( n, ' x ', c, ' = ', res)
print('Acabou')