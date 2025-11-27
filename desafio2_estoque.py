estoque = {
    "estoque": [
        {"codigoProduto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150},
        {"codigoProduto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75},
        {"codigoProduto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200},
        {"codigoProduto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320},
        {"codigoProduto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90}
    ]
}

mov_id = 1

def movimentar(codigo, quantidade, descricao):
    global mov_id

    for produto in estoque["estoque"]:
        if produto["codigoProduto"] == codigo:
            produto["estoque"] += quantidade

            print(f"\nMovimentação #{mov_id}")
            print(f"Descrição: {descricao}")
            print(f"Produto: {produto['descricaoProduto']}")
            print(f"Estoque final: {produto['estoque']}\n")

            mov_id += 1
            return

    print("Produto não encontrado.")

movimentar(101, 10, "Entrada de canetas")
movimentar(102, -5, "Baixa por venda")
movimentar(104, -12, "Perda")
