valores = []

while True:
    num =(int(input('Digite um valor: ')))
    if num in valores:
        print('Numero não adicionado por ja estar na lista')
    else:
        valores.append(num)
        print('Numero adicionado a lista')


    continuar = str(input('Quer continuar? [S/N]')).upper()
    if continuar == 'N':
        break
print(f'Você digitou {sorted(valores)}')