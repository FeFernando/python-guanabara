from random import randint

numeros = []

for c in range (0, 5):

    ale_num = randint(0, 10)
    numeros.append(ale_num)
maior = numeros[0]
menor = numeros[0]
for c in numeros:
    if c < menor :
        menor = c
    if c > maior:
        maior = c


print(numeros)
print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')