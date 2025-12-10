dados = list()
pessoas = list()
mai = men = 0
while True:
  nome = input('Digite o nome da pessoa: ')
  peso = int(input('Digite o peso da pessoa: '))
  dados.append(nome)
  dados.append(peso)
  pessoas.append(dados[:])

  if len(pessoas) == 1:
    mai = men = dados[1]
  else :
    if dados[1] > mai:
      mai = dados[1]
    if dados[1] < men:
      men = dados[1]

  dados.clear()

  choice = str(input('Deseja continuar? S/N')).upper()
  if choice == 'N':
    print(f'Foram cadastradas {len(pessoas)} pessoas')
    print(f'O maior peso foi {mai}. Peso de ', end='')
    for p in pessoas:
      if p[1] == mai:
        print(f'[{p[0]}]')
    print(f'O menor peso foi de {men}. Peso de ', end='')
    for p in pessoas:
      if p[1] == men:
        print(f'[{p[0]}]')