numeros = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'novo', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'deseseis', 'desessete', 'desoito', 'desenove', 'vinte',)

while True:
    num = int(input('Digite um numero: '))
    if num < 1 or num > 20:
        num = int(input('Numero invalido digite novamente!: '))
        continue

    for pos, digitado in enumerate(numeros, start=1):
        if num == pos:
            print(f'O numero que voce digitou foi {digitado}')