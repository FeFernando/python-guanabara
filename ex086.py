matriz = [
 [0, 0, 0,],
 [0, 0, 0,],
 [0, 0, 0,]
]
for i in range(3):
    for j in range(3):
        matriz[i][j]= int(input(f'Digite um numero para a posição [{i}] [{j}]: ' ))
print(matriz)