numeros=[]
while True:
    num = int(input("digite um numero ou [0] para sair:"))
    if num == 0:
        break
    else:
        numeros.append(num)
numeros.sort()
print(f"o maior valor da lista é: {numeros[-1]}")
print(f"o menor valor da lista é: {numeros[0]}")
print(f"lista na horizontal{numeros}")
print(f"lista na vertical mais indice:")
for i in numeros:
    print(f" o numero na posiçao {numeros.index(i)} é {i}")
