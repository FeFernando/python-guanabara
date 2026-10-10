valor = 10000

def verificar(num):
    qnt_falta = num * (100/valor)
    print(f'{qnt_falta}%')
    print('=' * int(qnt_falta) + '-' * (100 - int(qnt_falta)))




verificar(10000)