from random import randint

cont = 5
numeros = [randint(0, 10) for c in range(cont)]
maior = numeros[0]
menor = numeros[0]

for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(numeros)
print(f'O maior numero é {maior}')
print(f'O menor numero foi {menor}')