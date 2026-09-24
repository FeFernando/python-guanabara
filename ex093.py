relatorio = {}
lista_gols =[]
total_gols = 0
nome = str(input('Nome do jogador: '))
relatorio['nome'] = nome
partidas = int(input('Quantas partidas ele jogou?: '))

for i in range(partidas):
    gols_in_part = int(input(f'Quantos gols ele fez na {i+1}° partida?: '))
    lista_gols.append(gols_in_part)
    total_gols += gols_in_part
relatorio['list_gols'] = lista_gols

for i in relatorio:
    print(f'Nome do jogador: {relatorio['nome']}')
    for k in lista_gols:
        print(f'No {lista_gols.index(k)}° jogo ele fez {k} ')
print(f'Total de gols: {total_gols}')