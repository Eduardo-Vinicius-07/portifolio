n=((int(input("digite um numero:"))),(int(input("digite outro numero:"))),
   (int(input("digite mais um numero:"))),(int(input("digite o ultimo numero:"))),)
print(f"numeros digitados: {n}")
print(f"\no numero 9 apareceu: {n.count(9)} vezes")
if 3 in n:
    print(f"o numero 3 aparece a primeira vez na posiçao: {n.index(3)+1}")
else:
    print(f"o numero 3 nao apareceu")
print(f"os valores pares foram:", end="")
for i in n:
    if i % 2==0:
        print(i,end=" ")
