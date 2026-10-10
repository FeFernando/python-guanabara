def segura():
    res = 0
    while True:
        try:
            num = int(input('Digite o primeiro numero: '))
        except ValueError:
            print('VOCE NAO DIGITOU UM NUMERO!')
            break
        try:
            numTwo = int(input('Digite o segundo numero: '))
        except ValueError:
            print('VOCE NAO DIGITOU UM NUMERO!')
            break

        try:
            res = (num / numTwo)
        except ZeroDivisionError:
            print(' VOCE NAO PODE DIVIDIR POR ZERO')
            break

        print(f'O resultado é {res}')
        break

segura()
