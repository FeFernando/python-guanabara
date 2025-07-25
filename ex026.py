frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra a aparece {} vezes'.format(frase.count('a')))
print('A primeira aparece na posição {}'.format(frase.find('a')))
print('A ultima vez que aparece é na posição {}'. format(frase.rfind('a')))