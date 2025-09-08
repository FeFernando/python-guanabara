valores = []
for valor in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
maior = valores[0]
menor = valores[0]
posmaior = 0
posmenor = 0
for c, n in enumerate(valores):
    if n > maior:
        maior = n
        posmaior = c
    if n < menor:
        menor = n
        posmenor = c
print(f'O maior valor foi {maior} a posição dele é {posmaior}')
print(f'O menor valor foi {menor} a posição dele é {posmenor}')
print(valores)