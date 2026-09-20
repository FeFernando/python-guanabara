matriz = [
 [0, 0, 0,],
 [0, 0, 0,],
 [0, 0, 0,]
]

somapar = 0

somter = 0

maseg = 0
for i in range(3):



    for j in range(3):

        num = int(input(f'Digite um numero para a posição [{i}] [{j}]: ' ))

        if i == 1:
            if num > maseg:
                maseg = num

        if num % 2 == 0:
            somapar += num

        if j == 2:
            somter += num
        matriz[i][j] = num

print(matriz)
print(f'A soma de todos numeros pares é: {somapar}')
print(f'A soma dos numeros da terceira coluna é: {somter}')
print(f'O maior numero da segunda linha é: {maseg}')