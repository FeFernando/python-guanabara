import random

lista = []



numRep = int(input('Digite quantos jogos quer fazer: '))



for i in range(numRep):
    linha = []

    for j in range(6):
        numAle = random.randint(1, 60)
        linha.append(numAle)

        if numAle in linha[:-1]:
            linha.pop()

    lista.append(linha)


print(lista)