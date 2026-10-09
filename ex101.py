from datetime import date

hoje = date.today()
ano_atual = hoje.year


def voto(nascimento):
    idade = ano_atual - nascimento
    print(f'Você tem {idade}')

    if idade > 65 or 16 <= idade < 18:
        return 'SEU VOTO É OPCIONAL'
    elif  18 <= idade <65:
        return  'SEU VOTO É OBRIGATÓRIO'
    else:
        return 'VOTO NEGADO'


nas = int(input('Digite o ano em que nasceu: '))

res = voto(nas)
print(res)