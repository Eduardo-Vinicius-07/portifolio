turma=[]
while True:
    nota=int(input("digite a nota da prova do aluno ou [-1] para sair:"))
    if nota == -1:
        break
    else:
        turma.append(nota)
print(f"a media aritimetica da turma é: {sum(turma)/len(turma):.2f}")
print(f"a soma das notas da turma é: {sum(turma):.2f}")
