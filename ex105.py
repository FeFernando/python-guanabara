lista = {}

def notas(*num):
    maior = menor = num[0]
    soma = 0
    qtd = 0
    for i in num:
        soma += i
        if i > maior:
            maior = i
        if i < menor:
            menor = i

        qtd +=1
        media = soma / len(num)
    lista['total'] = qtd
    lista['maior'] = maior
    lista['menor'] = menor
    lista['media'] = media

notas(4, 2, 9, 7)
print(lista)