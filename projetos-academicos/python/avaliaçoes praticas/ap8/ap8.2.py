notas = []

while True:
    nota = float(input("Digite a nota do aluno (-1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

if len(notas) == 0:
    print("Nenhuma nota foi digitada.")
else:
    media = sum(notas) / len(notas)
    print(f"Quantidade de alunos: {len(notas)}")
    print(f"Média da turma: {media:.2f}")
