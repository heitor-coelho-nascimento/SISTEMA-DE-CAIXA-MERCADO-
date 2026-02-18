produtos = 'arroz', 'feijão'
precos = 'R$ 10.50', 'R$ 12.50'
carrinho = []
while True:
    print ('Selecione uma opção: "[i]nserir", "[a]pagar", "[c]arrinho"')
    opcao = input()

#inserir produtos na sua lista

    if opcao == 'i':
        for produto in enumerate(produtos):
            print(produto, precos)

        posicao =  int(input("Digite a posição: "))
        print(produtos, precos)
        produto = posicao
        carrinho.append(produto)

#lista dos produtos inseridos

    if opcao == 'c':
        for  produto in enumerate(carrinho):
            print(produtos)
   #         soma == (precosDeItensLista)

#apagar produtos na sua lista

    if opcao == 'a':
        for indice, excluirProduto in enumerate(carrinho):
            print(indice, produto)