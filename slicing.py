lista = []

while True:
    num = int(input('Digite um numero para adicionar a lista: '))
    lista.append(num)

    if num in lista[:-1]:
        lista.pop()

    esc = str(input('Deseja continuar?: S/N')).strip().lower()
    if esc != 's':
        break

print(lista)