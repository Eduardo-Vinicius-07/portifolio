sexo=""
while sexo not in ["M","F"]:
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo=="M":
        sexo="Masculino"
        break
    elif sexo=="F":
        sexo="Feminino"
        break
print(f"sexo {sexo} registrado com sucesso")
