
def leiaInt():
    while True:
        try:
            num = int(input('Digite um numero: '))

        except:
            print('\033[0;31mERRO DIGITE UM NUMERO INTEIRO!!\033[m')
        else:
            print(f'Você acabou de digitar o {num}')
            break


leiaInt()