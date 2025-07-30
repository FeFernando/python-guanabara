valor = int(input('Digite o valor da casa: '))
salario = float(input('Digite quanto você ganha: '))
tempo = int(input('Em quantos anos pretende pagar a casa? '))
meses = tempo * 12
prestacao = valor / meses

porcentagem = salario * 0.3

if prestacao > porcentagem :
    print('O valor das prestações ficaram a cima de R${} 30% de seu salario . Financiamento negado'.format(prestacao))
else:
    print('Aprovado, as parcelas ficaram R${:.2f}'.format(prestacao))