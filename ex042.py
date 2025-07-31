r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2 :
    print('As medidas de seu triangulo retangulo são {}, {}, {}'.format(r1, r2, r3))
    if r1 == r2 == r3:
        print('O seu triangulo é equilatero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
            print('Seu triangulo é isóceles')
    else:
            print('Seu triangulo é escaleno')
else:
    print('Não é possivel contruir um triangulo retangulo com essas medidas')
