from datetime import datetime

nascimento = int(input('Digite sua data de nascimento: '))

hoje = datetime.now().year

idade = hoje - nascimento
print(idade)
if idade < 9:
    print('Você é um atleta mirim')
elif  9 <= idade <= 14:
    print('Você é um atleta infantil')
elif  15 <= idade <= 19:
    print('Você é um atleta junior')
elif  19 <= idade <= 20:
    print('Você é um atleta senior')
else:
    print('Você é um atleta senior')