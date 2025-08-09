maior = 0
menor = 0
for c in range (1, 7):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {} e o menor peso é {}'.format(maior, menor))