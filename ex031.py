kmViagem = int(input('Digite quantos km terá sua viagem: '))
kmBaixo = 0.50
kmAlto =  0.45

if kmViagem < 201:
    print('O custo de sua viagem ficará em: {}'.format(kmBaixo*kmViagem))
else:
    print('O custo de sua viagem ficará em: {}'.format(kmAlto*kmViagem))