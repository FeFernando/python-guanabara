def tratamento(msg):
    while True:
        try:
            return float(input(msg).replace(',', '.'))
        except ValueError:
            print('ERRO AO ENCONTRAR NÚMERO! Tente novamente.')