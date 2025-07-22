from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja: '))
seno = sin(radians(angulo))
print('O seno desse angulo é: {:.2f}'.format(seno))
coseno = cos(radians(angulo))
print('O coseno dese angulo é: {:.2f}'.format(coseno))
tangente = tan(radians(angulo))
print('A tangente desse angulo é: {:.2f}'.format(tangente))