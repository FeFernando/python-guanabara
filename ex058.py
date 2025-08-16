import random

num_random = random.randint(1 , 11)
num_user = 0
cont = 0
while num_user != num_random :

    num_user = int(input('Qual numero eu pensei? '))
    if num_user < num_random:
        print('Mais... tente de novo')
    if num_user > num_random:
        print('Menos.. tente de novo')
    cont += 1
print('Acertou eu pensei no {}'.format(num_random))
print('Você precisou de {} tentativas para adivinhar.'.format(cont))