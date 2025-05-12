from time import sleep

def maior(*num):
    print("-=" * 30)
    print("Analisando os valores passados...")
    sleep(0.5)

    if len(num) == 0:
        print("Nenhum valor foi informado.")
        print("O maior valor informado foi: 0")
        return

    for valor in num:
        print(f"{valor} ", end='', flush=True)
        sleep(0.3)

    print(f"\nForam informados {len(num)} valor(es) ao todo.")
    print(f"O maior valor informado foi: {max(num)}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
