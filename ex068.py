from random import randint, choice

num = 0
choice = ''
res = 0
cont = 0
random_num = randint(1, 10)
while True:
    num = int(input('Digite um numero: '))
    choice = str(input('Par ou Impar? [P/I]: ')).upper().strip()

    res = random_num + num
    if choice == 'P' and res % 2 == 0:
        cont += 1
        print('Você ganhou!!')
    elif choice == 'I' and res % 2 == 1:
        cont += 1
        print('Você ganhou!!')
    else:
        print(random_num)
        print(res)
        print(f'Você perdeu, você ganhou {cont} vezes')
