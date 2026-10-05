from time import sleep

def maior(* num):
    cont = maior =0

    print('\nAnalisando os valores passados')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram informados {cont} valores ao todo\n')
    print(f'O maior valor informado foi {maior}\n')

maior(1, 2, 3, 4)

maior(5,6,7,8)
