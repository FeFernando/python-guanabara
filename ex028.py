import random

num = random.randint(1, 5)
userNum = int(input('Eu pensei em um numero, que numero foi esse? '))
if userNum == num :
    print('Você ganhou eu realmente pensei no {}'.format(userNum))
else:
    print('Eu ganhei você disse {} mas eu pensei {}'.format(userNum, num))