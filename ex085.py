lista = [
    [],
    []
]

for i in range(1,8):

    num = int(input('Digite um numero: '))

    if num % 2 == 0:
        lista[0].append(num)

    else:
        lista[1].append(num)


print(f'Os numeros pares são {lista[0]}')
print(f'Os numeros impares são {lista[1]}')