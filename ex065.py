res = 'S'
soma = cont = media = maior = menor =0

while res in 'sS' :
    num=int(input('Digite um numero: '))
    soma += num
    cont += 1
    if cont == 1 :
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor :
            menor = num
    res = input('Deseja continuar?[S/N]')
media = soma / cont
print('A media da soma dos numeros é {}'.format(media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))