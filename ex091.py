import random
tabela = []
jogador = 0
jogadores = {}
mainum= 0

for j in range(0, 4):
    num = random.randint(1, 6)
    jogador += 1
    jogadores['jogador'] = jogador
    jogadores['pontos'] = num
    tabela.append(jogadores.copy())
    if mainum == 0:
        mainum = num
    elif num > mainum:
        mainum = num
tabela.sort(key=lambda jogadores: jogadores["pontos"], reverse=True)
for j in tabela:
   print(f'O jogador {j["jogador"]} tirou {j["pontos"]} ')

print(f'O maior numero foi {mainum}')
print(tabela)