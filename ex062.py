ptermo = int(input('Digite o primeiro termo: '))
razao =  int(input('Digite a razão: '))
i = 1
total = 0
mais = 10
while mais !=0:
        total =total + mais
        while i <= total:
            print(ptermo, end=' ')
            ptermo += razao
            i += 1
        mais = int(input('\nQuantos termos você quer mostrar mais? '))



print('Fim!')