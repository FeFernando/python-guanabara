numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'novo', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)

while True:
    num = int(input('Digite um numero: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente')
print(f'O numero digitado é {numeros[num]}')