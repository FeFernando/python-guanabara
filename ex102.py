listFat=[]

def fatorial(nu, show=True):
    res = 1

    for i in range(1, nu+1):
        res *= i
        listFat.append(i)
    if show:
        for v in listFat:
            print(f'x {v} ', end='')
        print(f'= {res}')
    else:
        print(f'{res}')


num = int(input('Digite o numero: '))

fatorial(num)




