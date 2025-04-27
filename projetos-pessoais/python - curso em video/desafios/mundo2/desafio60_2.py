n=int(input("digite um numero: "))
fatorial=1
for c in range(n, 0, -1):
    fatorial*=c
print(f"o seu numero fatorial é {fatorial}")
