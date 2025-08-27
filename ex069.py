idade = 0
sexo = 0
maior = 0
homens = 0
mulher_menor = 0
choice_user = ''
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).upper().strip()
    while sexo not in ['F','M']:
        sexo = str(input('Sexo errado , digite o sexo [F/M]: ')).upper().strip()
    if idade > 18 :
        maior += 1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade < 20:
        mulher_menor +=1
    choice_user = str(input('Deseja continuar : [S/N]')).upper().strip()
    if choice_user == 'N':
        break
print(f'Existe {maior} maiores de idades na lista')
print(f'Existe {homens} homens na lista')
print(f'Existem {mulher_menor} mulheres menor de 20 anos na lista')