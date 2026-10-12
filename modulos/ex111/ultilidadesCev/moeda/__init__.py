def metade(n, formato=False):
    res = n / 2
    if formato:
        return f'R$ {n:.2f} '
    return res


def dobro(n, formato=False):
    res = n * 2
    if formato:
        return f'R$ {n:.2f} '
    return res


def aumento(n, v, formato=False):
    res = n * (v / 100) + n
    if formato:
        return f'R$ {n:.2f} '
    return res


def diminui(n, v, formato=False):
    res = n - (n * (v / 100))
    if formato:
        return f'R$ {n:.2f} '
    return res


def moeda(n):
    return f'R$ {n:.2f} '
def resumo(n, p1, p2):
    msg = 'RESUMO DO VALOR ex111'
    print(f'-'*len(msg) )
    print(msg)
    print(f'-' * len(msg) )
    print(f'{"Preço analisado":.<25} {moeda(n).replace('.', ','):>15}')
    print(f'{"O dobro do preço é":.<25} {moeda(dobro(n)).replace('.', ','):>15}')
    print(f'{"Metade do valor é":.<25} {moeda(metade(n)).replace('.', ','):>15}')
    print(f'{f"{p1}% de acrescimo":.<25} {moeda(aumento(n, p1)).replace('.', ','):>15}')
    print(f'{f"{p2}% de resução":.<25} {moeda(diminui(n, p2)).replace('.', ','):>15}')
