numeros = []

while True:
    n = int(input("Digite um número (-1 para parar): "))
    if n == -1:
        break
    numeros.append(n)

print(f"Quantidade de números digitados: {len(numeros)}")
