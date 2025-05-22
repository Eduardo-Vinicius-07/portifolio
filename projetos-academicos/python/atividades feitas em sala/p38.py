lista=[]
while True:
    x = int(input("digite um valor:"))
    if x== 9999:
        break
    else:
        lista.append(x)
print(f" lista na horizontal: {lista}")

print(f" lista na vertical:")
for i in lista:
    print(f"{i}")
print(f"quantidade de elementos na lista:{len(lista)}")
print(f"soma dos elementos na lista:{sum(lista)}")
print(f"maior valor na lista:{max(lista)}")
print(f"menor valor na lista:{min(lista)}")

y=int(input("digite um numero para saber se ele esta na lista: "))
if y in lista:
    print(f"o valor {y} esta na lista!\n na posição: {lista.index(y)}")
else:
    print(f"o valor {y} não esta esta na lista!")

lista.sort()
print(f"lista em ordem crescente: {lista}")

lista.insert(1,33) #insere o numero 33 na posição 1
print(lista)
lista.sort()

lista.reverse()
print(f"lista na ordem decrescente:{lista}")
lista.sort()
media= (sum(lista) / len(lista))
print(f"media dos valores da lista: {media:.3f}")
c=0
for j in lista:
    if j > 10:
        c+=1
print(f" tem {c} elementos maior que 10")
percentual=(c*100)/len(lista)
print(f"{percentual:.2f}% é maior que 10")
lista.remove(33)
print(lista)
