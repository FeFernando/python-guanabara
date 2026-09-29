time = list()
jogador = {}

total_gols = 0
while True:
    while True:
        lista_gols = []
        jogador.clear()
        jogador['nome'] = str(input('Nome do jogador: '))
        partidas = int(input('Quantas partidas ele jogou?: '))

        for i in range(partidas):
            gols_in_part = int(input(f'Quantos gols ele fez na {i+1}° partida?: '))
            lista_gols.append(gols_in_part)
        total_gols = sum(lista_gols)
        jogador['lista_gols'] = lista_gols
        jogador['total_gols'] = total_gols
        time.append(jogador.copy())


        esc = str(input('Deseja cadastrar mais jogador? S/N')).upper()[0]
        if esc in 'Nn':
            break

    for i in jogador.keys():
        print(f'{i:<15} ', end='')
    print()
    for k, v in enumerate(time):
        print(f'{k:>3}', end='')
        for d in v.values():
            print(f'{str(d):<15}', end='')
        print()

    choice = int(input('Qual jogador deseja ver o relatório (999 encerra programa)'))
    if choice >= len(time):
        print('Valor não encontrado digite outro : ')

    if choice == 999:
        break
    else:
        print(f'O relatório do jogador {choice} é: ')
        
