from datetime import datetime

current_datetime = datetime.now().year
maiores = 0
menores = 0
for c in range (1, 4):

    idade = int(input('Digite a data de nascimento da pessoa: '))
    if current_datetime - idade > 18:
        maiores +=1
    else:
        menores += 1
print('Existe {} pessoas maiores de idade'.format(maiores))
print('Existe {} pessoas menores de idade'.format(menores))