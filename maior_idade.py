maior_idade = 0
for i in range (0, 3):
    idade = int(input('Digite a idade'))
    if idade > maior_idade:
        maior_idade = idade
print('A maior idade é {}'.format(maior_idade))
