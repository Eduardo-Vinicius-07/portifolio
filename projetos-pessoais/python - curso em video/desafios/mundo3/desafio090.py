aluno = {}
aluno["nome"] = input("Nome: ")
aluno["media"] = float(input("media do aluno: "))
if aluno["media"] >= 7:
    aluno["situacao"] = "aprovado"
elif 7 > aluno["media"] >= 5:
    aluno["situacao"] = "recuperaçao"
else:
    aluno["situacao"] = "reprovado"

print(f"\n---boletim do aluno---")
for k, v in aluno.items():
    print(f"{k}: {v}")
