print("digite [-1] para sair")
ct=0
ap=0
rp=0
while True:
    n = float(input("digite a nota de um unico aluno:"))
    if n == -1:
        break
    ct+=1
    if n>=5:
        ap+=1
    if n<5:
        rp+=1
print("A quantidade de alunos que fizeram a prova:",ct)
print("quantidade de alunos aprovados:",ap)
print("quantidade de alunos reprovados:",rp)
