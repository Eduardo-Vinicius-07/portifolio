matriz = [[], [], []]

for linha in range(0,3):
    for coluna in range(0,3):
        valor = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        matriz[linha].append(valor)

print("\nMatriz 3x3:")
for linha in matriz:
    for valor in linha:
        print(f"[{valor:^5}]", end='')
    print()
