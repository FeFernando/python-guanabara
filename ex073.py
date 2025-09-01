times = (
    "Flamengo",    "Palmeiras",    "Cruzeiro",    "Bahia",    "Botafogo",    "Mirassol",    "São Paulo",
    "Red Bull Bragantino",    "Fluminense",    "Ceará",    "Corinthians",    "Atlético Mineiro",    "Internacional",
    "Grêmio",    "Santos",    "Vasco da Gama",    "Vitória",    "Juventude",    "Fortaleza",    "Sport"
)


print(f'Os cinco primeiros colocados são {times[:5]}')
print(f'Os quatros ultilmos colocados são {times[-4:]}')
ordemalfa = sorted(times)
print(f'Os nomes em ordem alfabetica {ordemalfa}')
nome = str(input('Digite o nome do time para ver sua posição na tabela: '))
for pos, time in enumerate(times, start=1):

    if nome == time:
        print(f'O {time} está na {pos}° posição!')