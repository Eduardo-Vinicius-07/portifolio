print("=" * 30)
print("      BANCO PYTHON      ")
print("=" * 30)

# Solicita o valor do saque
valor = int(input("Qual valor deseja sacar? R$ "))

# Definição das cédulas disponíveis
cedulas = [50, 20, 10, 1]
quantidades = {}

# Processa o saque
for cedula in cedulas:
    quantidade = valor // cedula  # Quantidade de cédulas do valor atual
    if quantidade > 0:
        quantidades[cedula] = quantidade
    valor %= cedula  # Atualiza o valor restante

# Exibe o resultado
print("\nVocê receberá:")
for cedula, quantidade in quantidades.items():
    print(f"{quantidade} cédula(s) de R${cedula}")

print("=" * 30)
print("      VOLTE SEMPRE!      ")
print("=" * 30)
