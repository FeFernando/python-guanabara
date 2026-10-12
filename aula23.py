try:
    a = int(input('Numerador: '))
    b = int(input('Denomindador: '))
    r = a / b
except Exception as error:
    print(f'Erro ao tentar dividir: {error}')
else:
    print(f'Resultado foi: {r}')