frase = str(input('Digite uma frase: ')).strip().upper()
list_world =  frase.split()
together = ''.join(list_world)
inverse = together[::-1]
if together == inverse :
    print('Essa frase é um palindromo')
else:
    print('Essa frase não é um palindromo')
print(together)