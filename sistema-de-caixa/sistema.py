produtos = 'arroz', 'feijão'
precos = 'R$ 10.50', 'R$ 12.50'
carrinho = []
while True:
    print ('Selecione uma opção: "[i]nserir", "[a]pagar", "[c]arrinho"')
    opcao = input()

#inserir produtos na sua lista

    if opcao == 'i':
        for indice, itens in enumerate(produtos):
            print(indice, itens, precos[indice])

        posicao = int(input("Digite a posição: "))
        print(produtos[posicao], precos[posicao])
    
        carrinho.append(itens)

#lista dos produtos inseridos

    if opcao == 'c':
        for  itens in enumerate(carrinho):
            print(itens)
   #         soma == (precosDeItensLista)

#apagar produtos na sua lista

    if opcao == 'a':
        for indice, excluirProduto in enumerate(carrinho):
            print(indice, itens)