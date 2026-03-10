# Sistema de controle de estoque para uma loja de eletrônicos

estoque = {}

def exibir_menu():
    print("===== MENU DE CONTROLE DE ESTOQUE =====")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Visualizar estoque")
    print("5 - Sair")

def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip()

    if nome in estoque:
        print("Produto já existe no estoque.")
        return

    try:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))

        estoque[nome] = {
            "preco": preco,
            "quantidade": quantidade
        }
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Erro: preço ou quantidade inválidos.")

def atualizar_produto():
    nome = input("Digite o nome do produto para atualizar: ").strip()

    if nome not in estoque:
        print("Produto não encontrado.")
        return

    try:
        preco = float(input("Digite o novo preço: "))
        quantidade = int(input("Digite a nova quantidade: "))

        estoque[nome]["preco"] = preco
        estoque[nome]["quantidade"] = quantidade
        print("Produto atualizado com sucesso!")
    except ValueError:
        print("Erro: preço ou quantidade inválidos.")

def excluir_produto():
    nome = input("Digite o nome do produto para excluir: ").strip()

    if nome in estoque:
        del estoque[nome]
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")

def visualizar_estoque():
    if not estoque:
        print("Estoque vazio.")
        return

    print("===== ESTOQUE ATUAL =====")
    for nome, dados in estoque.items():
        print(f"Produto: {nome}")
        print(f"Preço: R$ {dados['preco']:.2f}")
        print(f"Quantidade: {dados['quantidade']}")
        print("-" * 30)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()









