produtos = (
    'Arroz', 5.99,
    'Feijão', 7.50,
    'Macarrão', 4.20,
    'Óleo', 6.80,
    'Café', 12.00,
    'Açúcar', 3.90
)
print("=" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("=" * 40)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f"{nome:<30} R${preco:>7.2f}")

print("=" * 40)
