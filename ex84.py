galera = list()
teste = list()

nomapei = list()
nomenpe = list()
while True:
    teste.append(input('Nome: '))
    teste.append(float(input('Peso: ')))
    galera.append(teste[:])
    teste.clear()

    choice = input('Deseja continuar? S/N').strip().lower()

    if choice != 's':

        maipe = menpe = galera[0][1]

        for pessoas in galera:

            if pessoas[1] > maipe:
                maipe = pessoas[1]

            if pessoas[1] < menpe:
                menpe = pessoas[1]


        for pessoas in galera:

            if pessoas[1] == maipe:
                nomapei.append(pessoas[0])

            if pessoas[1] == menpe:
                nomenpe.append(pessoas[0])


        break

print(f'O maior peso foi {maipe} de {nomapei}')
print(f'O menor peso foi {menpe} de {nomenpe}')