from time import sleep


def contador(inicio, fim, passo):
    for i in range(inicio, fim +1, passo):
        print(f'{i}', end=' ')
        sleep(0.5)
    print()
contador(1, 10 ,1)
contador(10, -1,-2)



print('Agora é a vez de sua contagem:')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
if inicio > fim :
    passo = -passo
contador(inicio, fim, passo)



