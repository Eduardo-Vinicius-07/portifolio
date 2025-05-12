matriz = [[], [], []]
soma_pares = soma_terceira_coluna = 0
maior_segunda_linha = None

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)

        if valor % 2 == 0:
            soma_pares += valor

        if coluna == 2:
            soma_terceira_coluna += valor

        if linha == 1:
            if maior_segunda_linha is None or valor > maior_segunda_linha:
                maior_segunda_linha = valor

print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end='')
    print()

print(f"\nA) Soma dos valores pares: {soma_pares}")
print(f"B) Soma da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")
