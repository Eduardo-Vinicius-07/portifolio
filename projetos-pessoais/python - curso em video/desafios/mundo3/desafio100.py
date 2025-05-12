from random import randint
from time import sleep

numeros = []

def sorteia():
    print("Sorteando 5 números: ", end='')
    for _ in range(5):
        n = randint(1, 10)
        numeros.append(n)
        print(n, end=' ', flush=True)
        sleep(0.3)
    print()


def somapar():
    soma = sum(n for n in numeros if n % 2 == 0)
    print(f"A soma dos valores pares de {numeros} é {soma}")

sorteia()
somapar()