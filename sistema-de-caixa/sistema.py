produtos = 'arroz', 'feijão'
preco = 'R$ 10.50', 'R$ 12.50'
lista = []
while True:
    print ('Selecione uma opção: "[i]nserir", "[a]pagar", "[l]ista"')
    opcao = input()

    if opcao == 'i':
        for indice, produto in enumerate(produtos):
            print(indice, produto)
        print('Qual o número do produto que você quer?')
        selecionado = input()
            
    lista.append(selecionado)
    
    if opcao == 'l':
        for indice, produtoDaLista in enumerate(lista):
            print(indice, produtoDaLista)     

        if opcao == 'a':
            for indice, excluirProduto in enumerate(produtoDaLista):
                print(indice, produtoDaLista)  


