sexo = ''
while sexo != 'M' or 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo == 'M':
        print('Você é homem')
    if sexo == 'F':
        print('Você é mulher')
print('Acabou')
