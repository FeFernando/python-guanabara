elementos =  int(input('Quantidade de elementos: '))
i = 0
fibo = 0
t1 = 0
t2 = 1
while i < elementos:
    print(fibo, end=' ')
    fibo =  t1 + t2
    t1 = t2
    t2 = fibo
    i += 1
