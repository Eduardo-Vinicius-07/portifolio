from random import sample
from time import sleep

jogos = []

quantidade = int(input("Quantos jogos você quer gerar? "))

print("\nGerando seus palpites...\n")
for i in range(quantidade):
    jogo = sorted(sample(range(1, 61), 6))
    jogos.append(jogo)
    print(f"Jogo {i+1}: {jogo}")
    sleep(0.5)

print("\nBoa sorte! 🍀")
