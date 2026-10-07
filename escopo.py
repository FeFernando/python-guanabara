def test(b):
    global a #essa linha faz com que a variavel usada é a do escopo global sem ela teria como criar outra variavel a com valor diferente
    a = 5 #mesmo com essa declaração o que vale é a linha de cima
    




a = 8
test(a)