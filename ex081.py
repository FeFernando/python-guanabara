lista = []
while True:
    num = int(input('Digite um numero:'))
    lista.append(num)
    continuar= str(input('Deseja continuar? [S/N]')).upper()
    if continuar == 'N':
        break
print(f'Foram digitados {len(lista)}  numeros')
print(f'Os valores foram {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O numero 5 foi encontrado na lista')
else:
    print('O numero 5 não esta na lista')