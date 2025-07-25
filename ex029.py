vel = int(input('Digite sua velocidade '))
limite = 80
valMulta = 7

if vel > limite:
    km_acima= vel - limite
    valorMulta = km_acima * valMulta
    print('Voce foi multado em {}R$ '.format(valorMulta))
else:
    print('Você esta dentro do limite')