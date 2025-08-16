sexo = ''
sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Sexo errado digite novamente [M/F]: ')).upper()

print('Sexo {} registrado com sucesso')

