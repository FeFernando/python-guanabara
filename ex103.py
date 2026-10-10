def ficha(nome='desconhecido', gols=0):
    if nome == '':
        nome = 'desconhecido'
    if gols == '':
        gols = 0
    else:
        gols = int(gols)
    print(f'O jogador {nome} fez {gols} gols neste campeonato')

nomeInput = input('Digite o nome do jogador: ')
golsInput = input('Quantos gols ele fez no campeonato?: ')

ficha(nomeInput, golsInput)