pessoas_cadastradas = []
media_idade = 0

acima_media = []


while True:
    nome = str(input('Nome: '))
    idade = int(input('Idadae: '))
    sexo = str(input('Sexo F/M: ')).strip().lower()
    choice = str(input('Deseja continuar? s/n: ')).strip().lower()

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

        media_idade = (soma / len(pessoas_cadastradas))
        for user in pessoas_cadastradas:
            if user['idade'] > media_idade:
                acima_media.append(user)

        print(f'{soma}')
        print(f'{media_idade}')
        print(f'{acima_media}')

        break
print(30*'-=')
print()
print(f'-O grupo tem {len(pessoas_cadastradas)} pessoas.')
print(f'-A media de idade é de {media_idade} anos.')
print('-As mulheres cadastradas foram.', end='')
for p in pessoas_cadastradas:
    if p['sexo'] == 'f':
        print(f'{p['nome']}', end='')
print('Lista de pessoas que estão acima da média de idade:')
for acim in acima_media:
    print(f'Nome: {acim["nome"]}, Idade: {acim["idade"]}')