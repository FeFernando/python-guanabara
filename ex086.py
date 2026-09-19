matriz = [
 [0, 0, 0,],
 [0, 0, 0,],
 [0, 0, 0,]
]

for i in range(3):

    for j in range(3):

        num = int(input(f'Digite um numero para a posição [{i}] [{j}]: ' ))
        matriz[i][j] = num

print(matriz)