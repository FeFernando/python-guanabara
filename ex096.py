valores = []

def area(lista):
    res = 1
    for valor in lista:
        res *= valor
    print(f'A area de um terreno {lista[0]}x{lista[1]} é de {res}m².')


print('Controle de Terrenos')
print('-'*20)
valores.append( float(input('LARGURA (m): ')))
valores.append( float(input('COMPRIMENTO (m): ')))

area(valores)