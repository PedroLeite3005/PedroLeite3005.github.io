totalProdutos = []
produtos = [
    ["Coca-Cola", 3.75, 2],
    ["Pepsi", 3.67, 5],
    ["Monster", 9.96, 1],
    ["Café", 1.25, 100],
    ["Redbull", 13.99, 2]
]
moeda = [
    ["Nota de R$20", 20, 5],
    ["Nota de R$10", 10, 5],
    ["Nota de R$5", 5, 5],
    ["Nota de R$2", 2, 5],
    ["Moeda de R$1", 1, 5],
    ["Moeda de R$0,50", 0.50, 10],
    ["Moeda de R$0,25", 0.25, 10],
    ["Moeda de R$0,10", 0.10, 10],
    ["Moeda de R$0,05", 0.05, 10],
    ["Moeda de R$0,01", 0.01, 10]
]


def mostrar_menu():
    """a funcao serve para apresentar os produtos no menu da maquina de vendas"""
    print("======== Máquina de Vendas ========")
    print("0. Sair")
    for i, produto in enumerate(produtos): # numerar os produtos da lista
    # o enumerate retorna o index da linha e a linha como uma lista, por isso e possivel chamar posicoes
        print(f"{i + 1}. {produto[0]} - R$ {produto[1]} - Estoque: {produto[2]}") # serve para fornecer a informacao de cada produto na tela
    print(f"{len(produtos)+1}. Concluir")
    print("===================================")


def verificar_troco(troco):
    """a funcao serve para calcular o troco necessario, dependendo do valor que o usuario insere"""
    troco = int(troco * 100)  # Converter o valor do troco para centavos
    trocoTotal = 0
    print("Troco:")
    for i in range(len(moeda)):
        trocoTotal += (moeda[i][1] * moeda[i][2])
        if trocoTotal < troco:
            for i, item in enumerate(moeda): # percorre as moedas e faz as verificacoes
                nome = item[0]
                valor = int(item[1] * 100)  # Converter o valor da moeda para centavos
                estoque = item[2]
                quantidade = troco // valor
                if quantidade > estoque:
                    quantidade = estoque  # limita a quantidade de notas a ser utilizadas
                    print("troco insuficiente")
                    break
                if quantidade > 0:
                    troco -= quantidade * valor # serve para calcular o troco
                    estoque -= quantidade # serve para atualizar o estoque de moedas
                    print(f"{quantidade} x {nome}, Estoque: {estoque}")
                if troco == 0: # se o troco e 0 n tem ele dar troco
                    break


def realizar_compra(produto):
    if produto >= 1 and produto <= len(produtos): # serve para n comecar no zero e pegar o tamanho maximo da matriz
        produto_escolhido = produtos[produto - 1] # serve para corrigir o index. ex: se vc digitar 1 "coca-cola" iria atribuir o valor da pepsi
        nome = produto_escolhido[0]
        preco = produto_escolhido[1]
        estoque = produto_escolhido[2]
        if estoque > 0:
            produto_escolhido[2] -= 1  # abaixa o estoque
            mostrar_menu()
            print(f"Você comprou {nome} por R$ {preco:.2f}.")
            totalProdutos.append(produto_escolhido[1]) # da append no preco
        else:
            print(f"A quantidade do {nome} no estoque acabou!")
        total = sum(totalProdutos) # serve pra atualizar a quantidade de produto que tem disponivel
        print(f"O total é: R$ {total:.2f}")


def maquina_compra():
    mostrar_menu()
    while True:
        opcao = int(input("Insira a ID do produto: "))
        total = sum(totalProdutos)
        if opcao == 0:
            print("Saindo da máquina de vendas!")
            break
        elif opcao == len(produtos)+1:
            print("Hora do pagamento!")
            pagamento = float(input("Digite o valor que você dará a máquina: "))
            if pagamento < total:
                print("Valor insuficiente. Compra cancelada!")
            elif pagamento >= total:
                troco = pagamento - total
                print("Ok! Prosseguindo para o troco!")
                print(f"Seu troco é: R${troco:.2f}")
                verificar_troco(troco)
            break
        elif opcao > len(produtos):
            print("Número inválido!")
        elif opcao == -1:
            modo_admin()
        else:
            realizar_compra(opcao)


def modo_admin():
    while True:
        print("======== Modo Administrador ========")
        print("0. Voltar")
        print("1. Adicionar item")
        print("2. Editar item")
        print("3. Excluir item")
        opcao = int(input("Insira a opção desejada: "))
        if opcao == 0:
            mostrar_menu()
            break
        elif opcao == 1:
            nome = input("Insira o nome do novo produto: ")
            preco = float(input("Insira o preço do novo produto: "))
            estoque = int(input("Insira o estoque do novo produto: "))
            produtos.append([nome, preco, estoque])
            print("Novo produto adicionado com sucesso!")
        elif opcao == 2:
            mostrar_menu()
            indice = int(input("Insira o ID do produto que deseja editar: "))
            if indice >= 1 and indice <= len(produtos):

                nome = input("Insira o novo nome do produto: ")
                preco = float(input("Insira o novo preço do produto: "))
                estoque = int(input("Insira o novo estoque do produto: "))
                produtos[indice - 1][0] = nome # atribui um novo valor a posicao [i][j] da matriz
                produtos[indice - 1][1] = preco
                produtos[indice - 1][2] = estoque
                print("Produto editado com sucesso!")
            else:
                print("Índice inválido!")
        elif opcao == 3:
            mostrar_menu()
            indice = int(input("Insira o ID do produto que deseja excluir: "))
            if indice >= 1 and indice <= len(produtos):
                produto = produtos.pop(indice - 1) # a funcao pop retorna o valor deletado(produto), para consiguir "chama-lo" no proximo print
                print(f"O produto {produto[0]} foi excluído com sucesso!")
            else:
                print("Índice inválido!")
        else:
            print("Opção inválida!")


maquina_compra()