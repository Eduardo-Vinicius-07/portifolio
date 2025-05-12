from datetime import datetime

cadastro = {}

cadastro["nome"] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
cadastro["idade"] = datetime.now().year - nascimento
cadastro["ctps"] = input("Carteira de trabalho (0 = não tem): ")

if cadastro["ctps"] != "0":
    cadastro["contratacao"] = int(input("Ano de contratação: "))
    cadastro["salario"] = float(input("Salário: R$"))
    cadastro["aposentadoria"] = cadastro["contratacao"] + 35 - nascimento

print("\n--- Cadastro Final ---")
for k, v in cadastro.items():
    print(f"{k:<15}: {v}")
