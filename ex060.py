num = int(input('Digite um numero: '))
c = num
fat = 1
for c in range (c, 0, -1):
    print(c, 'x ' , end='')
    fat *= c
print('O fatorial de {} é {}'.format(num, fat))







'''i = num
fat = 1
while i >=1:
    print(i)
    fat = fat * i
    i -=1
print(fat)'''
