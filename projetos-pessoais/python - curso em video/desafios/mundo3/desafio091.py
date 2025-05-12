from random import randint
from time import sleep
jogo={ "jogador 1": randint(1, 6),
    "jogador 2": randint(1, 6),
      "jogador 3": randint(1, 6),
      "jogador 4": randint(1, 6) }

print(f"valores sorteados:")
for j, v in jogo.items():
    print(f"{j} tirou: {v}")
    sleep(0.5)

ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)

print("\n--- Ranking dos jogadores ---")
for i, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{i}º lugar: {jogador} com {valor}")
    sleep(0.5)
    