frase = []

def riscar(frase):
    for palavra in frase:
        print(f'-'*len(palavra))
        print(f'{palavra}')
        print(f'-'*len(palavra))


palavras = str(input('Digite dua frase ou palavra: '))
frase.append(palavras)

riscar(frase)
