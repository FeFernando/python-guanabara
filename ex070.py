total = 0
maidemil = 0
barato = ''
menor_preco = 0
while True:
    produto = str (input('Digite o nome do produto: '))
    preco = float(input('Qual o preço do produto: '))
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    total += preco
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        barato = produto

    if preco > 1000:
        maidemil += 1
    if continuar == 'N':
        break
print(f'O total gasto na compra foi {total}')
print(f'Foram comprados {maidemil} produtos acima de mil reais!')
print(f'O produto mais barato foi {barato}')