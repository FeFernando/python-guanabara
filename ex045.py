import random

print('Qual a sua escolha?')
print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')
user_choice = int(input(': '))
pc_choice = random.randint(1, 3)
print('O computador escolher {}'.format(pc_choice))

if user_choice == 1 and pc_choice == 2 or user_choice == 2 and pc_choice == 3 or user_choice == 2 and pc_choice == 3 :
    print('Você perdeu')

elif user_choice == 1 and pc_choice == 3 or user_choice == 2 and pc_choice == 1 or user_choice == 3 and pc_choice == 2:
    print('Você ganhou!')
elif user_choice == pc_choice:
    print('Deu empate!')
else:
    print('Escolha errada')