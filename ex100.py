import random

lista = list()
def sortear():
    for i in range(5):
        numSort = random.randint(0, 10)
        lista.append(numSort)

sortear()
print(f'Numeros sorteados {lista}')
def somaPar():
    par = 0
    for n in lista:
        if n % 2 == 0:
            par += n

    print(f'A soma dos numeros pares é {par}')


somaPar()


