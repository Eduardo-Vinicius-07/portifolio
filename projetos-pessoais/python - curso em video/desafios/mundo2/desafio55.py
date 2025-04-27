maior_peso=0
menor_peso=9999999
for c in range(1,6):
    peso=float(input("qual o seu peso: "))
    if maior_peso<peso:
        maior_peso=peso
    if menor_peso>peso:
        menor_peso=peso
print(f"o maior peso foi de {maior_peso}kg\n e o menor peso foi de {menor_peso}kg")
m