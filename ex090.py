aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('Media do aluno: '))

if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'

print(f'O nome é igual a {aluno["nome"]}')

print(f'Média é igual a {aluno["media"]}')

print(f'A situação é igual a {aluno["situacao"]}')