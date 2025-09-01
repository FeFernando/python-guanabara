palavras = ('Programar', 'Rodizio', 'Caixote')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print(f'\nA palavra {palavra} tem ', end='')
    for letra in palavra.lower():
        if letra in vogais:
            print(f' {letra} ', end='')

