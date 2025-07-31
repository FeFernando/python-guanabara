peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura  * altura)
print(imc)
if imc < 18.5 :
    print('Você esta muito abaixo do ideal')
elif 18.5 <= imc <= 25:
    print('Você esta com o peso ideal')
elif 25 <= imc <= 30:
    print('Você esta com sobrepeso')
elif 30 <= imc <= 40:
    print('Você esta obeso')
else:
    print('Você esta com obesidade morbida')