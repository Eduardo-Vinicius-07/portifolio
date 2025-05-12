pessoas = []
maior = menor = 0

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    continuar = input("Quer continuar? [S/N] ").strip().lower()
    if continuar == 'n':
        break

print(f"\nA) Total de pessoas cadastradas: {len(pessoas)}")

print(f"B) Peso máximo: {maior:.1f}kg. Pessoas mais pesadas:", end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]", end=' ')

print(f"\nC) Peso mínimo: {menor:.1f}kg. Pessoas mais leves:", end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]", end=' ')
