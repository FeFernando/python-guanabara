lista = []


while True:
    nomes = []
    notas = []
    medias = []

    nome = str(input('Digite o nome do aluno: '))
    nomes.append(nome)
    for i in range(1, 3):
        nota = float(input(f'Nota {i}: '))
        notas.append(nota)
    media = sum(notas)/2
    medias.append(media)
    lista.append([nome, notas, medias])


    esc = str(input('Deseja continuar? S/N: ')).strip().lower()
    if esc != 's':
        break
for i in range(len(lista)):
    print(f'N°:{i} Nome:{lista[i][0]}   Media:{lista[i][2]} \n')

while True:
    exi = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe)'))

    if exi == 999:
        break
    else:
        print(f'Notas de {lista[exi][0]} são {lista[exi][1]}')