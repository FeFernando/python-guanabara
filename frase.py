palavra_uni = ''

frase = str(input('Digite uma frase: ')).lower()
partes = frase.split()


if partes.count(frase) == 1:
    palavra_uni = frase
print('As palavras unicas são{}'.format(palavra_uni))
print(len(partes))