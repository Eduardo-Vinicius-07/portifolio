from time import sleep

def contador(inicio, fim, passo):
    print("-=" * 20)
    print(f"Contando de {inicio} até {fim} de {abs(passo)} em {abs(passo)}")
    sleep(1)

    if passo == 0:
        passo = 1

    if inicio < fim:
        for c in range(inicio, fim + 1, abs(passo)):
            print(c, end=" ", flush=True)
            sleep(0.3)
    else:
        for c in range(inicio, fim - 1, -abs(passo)):
            print(c, end=" ", flush=True)
            sleep(0.3)
    print()


contador(1, 10, 1)
contador(10, 0, 2)

print("-=" * 20)
print("Agora é sua vez de personalizar a contagem!")
contador((int(input("inicio:"))),int(input("fim:")),int(input("passo:")))
