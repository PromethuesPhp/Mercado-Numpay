import statistics

lista_vendas = []


def cadastrar_venda():
    while True:
        produto = input("Nome do produto (ou ENTER para voltar ao menu): ")
        if produto.strip() == "":
            break

        while True:
            entrada_preco = input("Preço: ")
            try:
                preco = float(entrada_preco.replace(",", "."))
                if preco < 0:
                    print(" O preço não pode ser negativo.")
                    continue
                break
            except ValueError:
                print(" Valor inválido! Digite um número (ex: 4.50).")

        while True:
            entrada_qtd = input("Quantidade: ")
            try:
                quantidade = int(entrada_qtd)
                if quantidade <= 0:
                    print(" A quantidade precisa ser maior que zero.")
                    continue
                break
            except ValueError:
                print(" Valor inválido! Digite um número inteiro (ex: 3).")

        lista_vendas.append((preco, produto, quantidade))
        print(f" {quantidade}x {produto} — R$ {preco:.2f} cada, adicionado!\n")


def mostrar_resultado():
    if len(lista_vendas) == 0:
        print("\nNenhuma venda registrada ainda.\n")
        return

    precos = [venda[0] for venda in lista_vendas]
    quantidades = [venda[2] for venda in lista_vendas]
    subtotais = [preco * qtd for preco, qtd in zip(precos, quantidades)]

    total_faturado = sum(subtotais)
    total_itens = sum(quantidades)
    media = statistics.mean(precos)
    mediana = statistics.median(precos)
    moda = statistics.mode(precos)

    nome_produto_moda = next(
        venda[1] for venda in lista_vendas if venda[0] == moda
    )

    print("\n--- Resultado do dia ---")
    print(f"Total de itens vendidos: {total_itens}")
    print(f"Total faturado: R$ {total_faturado:.2f}")
    print(f"Preço médio: R$ {media:.2f}")
    print(f"Mediana de preço: R$ {mediana:.2f}")
    print(f"Moda (valor mais comum): R$ {moda:.2f} — {nome_produto_moda}")
    print("------------------------\n")


def menu():
    while True:
        print("=== MENU ===")
        print("1 - Baixas do dia")
        print("2 - Resultado do dia")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_venda()
        elif opcao == "2":
            mostrar_resultado()
        elif opcao == "3":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print(" Opção inválida. Digite 1, 2 ou 3.\n")


if __name__ == "__main__":
    menu()