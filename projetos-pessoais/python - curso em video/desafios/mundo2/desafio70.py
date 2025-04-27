total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ""
preco_mais_barato = float('inf')

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$"))

    # Atualiza o total gasto
    total_gasto += preco

    # Conta produtos que custam mais de R$1000
    if preco > 1000:
        produtos_acima_1000 += 1

    # Verifica o produto mais barato
    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja continuar? [S/N]: ").strip().upper()
    if continuar == "N":
        break

# Exibe os resultados
print("\n===== RESUMO DA COMPRA =====")
print(f"Total gasto na compra: R${total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$1000: {produtos_acima_1000}")
print(f"Produto mais barato: {produto_mais_barato} (R${preco_mais_barato:.2f})")
