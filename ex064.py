dig = ''
cont = 0
soma = 0
while dig !=999:
    dig = int(input('Digite o numero: '))
    cont += 1
    soma += dig
print('Foi digitados {} numeros e a soma deles é {}'.format(cont, soma-999))