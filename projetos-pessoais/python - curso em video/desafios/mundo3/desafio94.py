grupo = []
soma_idades = 0
while True:
    pessoa = {}

    pessoa['nome'] = input("Nome: ")
    pessoa['sexo'] = input("Sexo [M/F]: ").strip().upper()
    while pessoa['sexo'] not in ['M', 'F']:
        pessoa['sexo'] = input("Sexo inválido. Digite M ou F: ").strip().upper()

    pessoa['idade'] = int(input("Idade: "))
    soma_idades += pessoa['idade']

    grupo.append(pessoa.copy())

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input("Resposta inválida. Digite S ou N: ").strip().upper()
    if continuar == 'N':
        break

media = soma_idades / len(grupo)

print(f"\nA) Total de pessoas cadastradas: {len(grupo)}")

print(f"B) Média de idade do grupo: {media:.2f} anos")

print("C) Lista de mulheres:")
for p in grupo:
    if p['sexo'] == 'F':
        print(f"   {p['nome']}")

print("D) Lista de pessoas com idade acima da média:")
for p in grupo:
    if p['idade'] > media:
        print(f"   Nome: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}")
