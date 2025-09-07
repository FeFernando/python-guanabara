num = (int(input('Digite um numero: ')),
 int(input('Digite outro numero: ')),
 int(input('Digite mais um numero: ')),
 int(input('Digite o ultimo numero: ')))
par = 0
for n in num:
    if n % 2 == 0:
        par+=1


print(f'O numero 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na posição {num.index(3)+1}')
print(f'A quantidade de numeros pares foram {par}')