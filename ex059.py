val1 = 0
val2 = 0
choice = 0
soma = 0
mult = 0
maior = 0
while choice == 0 :
    val1 = int(input('Digite o primeiro valor: '))
    val2 = int(input('Digite o segundo valor: '))
    print(' [1]Somar \n [2]Mutiplicar \n [3]Maior \n [4]Novos numeros \n [5]Sair do programa')
    choice = int(input('Digite o numero referente ao comando:'))
    if choice == 1:
        soma = val1 + val2
        print('A soma dos dois valores é {}'.format(soma))
    if choice == 2:
        mult = val1 * val2
        print('A multiplicação dos dois numero é {}'.format(mult))
    if choice == 3:
        maior = val1
        if val2 > val1:
            print('O {} é maior que o {}'.format(val2, val1))
        else:
            print('O {} é maior que {}'.format(val1, val2))
    if choice == 4:
        