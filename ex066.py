n = 0
soma = 0
cont = 0
while True:
    n = int(input('Digite o numero: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} numeros')
print(f'A soma dos numeros é {soma}')