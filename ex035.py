t1 = float(input('Digite o tamanho da primeira linha: '))
t2 = float(input('Digite o tamaho da segunda linha: '))
t3 = float(input('Digite o tamanho da terceira linha: '))

if t1 + t2 > t3 and t1 + t3 > t2 and t3  + t2 > t1 :
    print('Com essas medidas é possivel formar um triangulo')
else:
    print('Com essas medidas não é possivel formar um triangulo')