from datetime import datetime

nascimento = int(input('Digite o ano em que nasceu: '))
ano_agora = datetime.now().year
idade =  ano_agora - nascimento

if idade < 18 :
    print('Você tem {} anos'.format(idade))
    falta = 18 - idade
    print('Ainda falta {} anos para você se alistar'.format(falta))
elif idade > 18:
    atrasado = idade - 18
    print('Você deveria ja ter se alistado')
    print('Você está atrasado em {} anos'.format(atrasado))


