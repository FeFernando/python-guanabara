def metade(n, formato=False):
     res = n / 2
     if formato:
         return f'R$ {n:.2f} '
     return res

def dobro(n, formato = False):
    res = n * 2
    if formato:
        return f'R$ {n:.2f} '
    return res

def aumento(n, v, formato = False):
    res = n *(v/100) + n
    if formato:
        return f'R$ {n:.2f} '
    return res

def diminui (n, v, formato = False):
    res = n- (n *(v/100))
    if formato:
        return f'R$ {n:.2f} '
    return res
def moeda(n):
    return f'R$ {n:.2f} '

