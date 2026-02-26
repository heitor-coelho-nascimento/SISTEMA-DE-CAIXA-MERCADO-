produtos = 'arroz', 'feijão'
precos = 'R$ 10.50', 'R$ 12.50'
carrinho = []
while True:
    print ('Selecione uma opção: "[i]nserir", "[a]pagar", "[c]arrinho"')
    opcao = input()

    #inserir produtos na sua lista

    if opcao == 'i':
        for indice, produto in enumerate(produtos):
            print(indice, produto, "-", precos[indice])

        posicao = int(input("Digite a posição: "))

        item = (produtos[posicao], precos[posicao])
        carrinho.append(item)

        print('Adicionado', item)
    #lista dos produtos inseridos

    if opcao == 'c':
        for  indice, item in enumerate(carrinho):
            print(indice, item[0], '-', item[1])

   #         soma == (precosDeItensLista)

    #apagar produtos na sua lista

    if opcao == 'a':
        for indice, item in enumerate(carrinho):
            print(indice, item[0], "-", item[1])

        posicao = int(input("Digite o índice para remover: "))
        carrinho.pop(posicao)