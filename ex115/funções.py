def menu():
    while True:
        msgMenu = 'MENU PRINCIPAL'
        print('-' * 30)
        print(f'{msgMenu:^30}')
        print('-' * 30)

        print(f'1 - Ver pessoas cadastradas')
        print(f'2 - Cadastrar nova pessoa')
        print(f'3 - Sair do sistema')
        print('-' * 30)
        num = int(input('Sua opção: '))

        if num == 1 :
            cadastrados()
        elif num == 2 :
            cadastrar()
        elif num == 3:
            break

def cadastrados():
    print('-' * 30)
    print(f'{'PESSOAS CADASTRADAS':^30}')
    print('-' * 30)

    with open('pessoas.text', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(';')
            print(f'Nome: {nome} | Idade: {idade}')

def cadastrar():
    with open('pessoas.text', 'a', encoding='utf-8') as arquivo:
        while True:
            print('-' * 30)
            print(f'{'NOVO CADASTRO':^30}')
            print('-' * 30)

            nome = str(input('NOME: '))

            try:
                idade = int(input('IDADE: '))
            except:
                print('VALOR INVALIDO!')
            else:
                arquivo.write(f'{nome}; {idade}\n')
                print('PESSOA CADASTRADA')
                break


