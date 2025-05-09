lista = []
for i in range(0,5):
    lista.append(int(input("Digite um valor: ")))

maior = max(lista)
menor = min(lista)

print(f"\nO maior valor foi {maior} nas posições: ", end='')
for i, v in enumerate(lista):
    if v == maior:
        print(i, end=' ')

print(f"\nO menor valor foi {menor} nas posições: ", end='')
for i, v in enumerate(lista):
    if v == menor:
        print(i, end=' ')
