

produtos = []
while True:

    print('==== MENU ====')
    op = int(input(' 1 - Cadastrar Produto \n 2 - Listar produto \n 3 - Vender produto \n 4 - Sair \n Escolha: '))

    if op == 1:
        nome_produto = str(input('Digite o nome do Produto: '))
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço: '))
        produto = {"nome": nome_produto, "quantidade": quantidade, "preco": preco}
        produtos.append(produto)
        print('Produto cadastrado com sucesso!!')

    if op == 2:
        for p in produtos:
            print(f"{p['nome']:<10} | {p['quantidade']:<10} | R$ {p['preco']:.2f}")
            print()