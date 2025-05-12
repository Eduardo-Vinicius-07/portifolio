lista = []
for i in range(5):
    valor = int(input("Digite um valor: "))

    if i == 0 or valor > lista[-1]:
        # Se for o primeiro ou maior que o último, adiciona no fim
        lista.append(valor)
        print("Adicionado ao final da lista.")
    else:
        # Procura a posição correta para inserir
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f"Adicionado na posição {pos} da lista.")
                break
            pos += 1

print(f"\nOs valores digitados em ordem foram: {lista}")
