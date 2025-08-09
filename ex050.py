soma = 0
for n in range (0, 6):
    num = int(input('Digite um numero'))
    print(soma)
    if num % 2 == 0:
        soma = soma + num
print('A soma dos numeros pares é {}'.format(soma))