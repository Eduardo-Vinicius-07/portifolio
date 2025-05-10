alunos = []

while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    cont = input("Deseja continuar? [S/N] ").strip().lower()
    if cont == 'n':
        break

print(f"\n{'Nº':<5} {'NOME':<10} {'MÉDIA':>6}")
print("-" * 25)
for i, aluno in enumerate(alunos):
    print(f"{i:<5} {aluno[0]:<10} {aluno[2]:>6.1f}")

while True:
    opc = int(input("\nMostrar notas de qual aluno? (999 para parar): "))
    if opc == 999:
        print("Finalizando...")
        break
    if 0 <= opc < len(alunos):
        print(f"Notas de {alunos[opc][0]}: {alunos[opc][1]}")
    else:
        print("Número inválido!")
