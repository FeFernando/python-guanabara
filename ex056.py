media = 0
soma = 0
maior_idade = 0
nome_maior_idade = ''
sum_idade_mulher= 0
cont = 0
for i in range (0, 3):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M] para homen [F] para mulher')).upper()
    soma += idade
    media = soma / 3
    if sexo == 'M' and idade > maior_idade:
        maior_idade =  idade
        nome_maior_idade = nome
    if sexo == 'F':
        sum_idade_mulher += idade
        cont = cont + 1

if nome_maior_idade:
    print('O homen mais velho é {}'.format(nome_maior_idade))
if sum_idade_mulher:
    print('A soma da idade das mulheres é {}'.format(sum_idade_mulher))
    print('Existem {} mulheres'.format(cont))
print('A media das idades é: {}'.format(media))