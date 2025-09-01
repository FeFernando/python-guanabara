carros = ('Polo', 95.790, 'Onix', 93.770, 'Argo', 89.990, 'Kwid', 77.240, 'Mobi', 77.990)

for pos in range(0, len(carros)):
    if pos % 2 == 0:
        print(f'{carros[pos]:.<15}', end='')
    else:
        print(f'{carros[pos]:.3f}')