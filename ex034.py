salario = float(input('Digite o seu salario: '))

if salario < 1250 :
    quinze = salario * 0.15
    print('Seu salario com 15% de aumento ficará: {}'.format(salario + quinze))
else:
    dez = salario *0.10
    print('Seu salario com aumento de 10% é: {} '.format(salario+dez))