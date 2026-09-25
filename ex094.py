pessoas_cadastradas = []
total_pessoas = 0
media_idade = 0
todas_mulheres = []
acima_media = []
while True:
    nome = str(input('Nome: '))
    idade = int(input('Idadae: '))
    sexo = str(input('Sexo F/M: ')).strip().lower()
    total_pessoas +=1
    choice = str(input('Deseja continuar? s/n: ')).strip().lower()

    if sexo == 'f':
        todas_mulheres.append(nome)



    pessoa = {
        "nome" : nome,
        "idade": idade,
        "sexo": sexo

    }

    pessoas_cadastradas.append(pessoa)

    if choice != 's':
        soma = 0
        for pesso in pessoas_cadastradas:
            soma += pesso['idade']

        media_idade = soma / total_pessoas
        if pessoa['idade'] > media_idade:
            acima_media.append(pessoa)

        print(f'{soma}')
        print(f'{media_idade}')
        print(f'{acima_media}')

        break
print(30*'-=')
print()
print(f'-O grupo tem {total_pessoas} pessoas.')
print(f'-A media de idade é de {media_idade} anos.')
print(f'-As mulheres cadastradas foram {todas_mulheres}.')
print('Lista de pessoas que estão acima da média de idade:')
for acim in acima_media:
    print(f'Nome: {acim}')