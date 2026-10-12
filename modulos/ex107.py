import moeda

num = float(input('Digite o numero: '))
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'Aumentando 10%, temos {moeda.aumento(num, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminui(num, 13)}')