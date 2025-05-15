def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} marcou {gols} gol(s).")


n = input("Nome do jogador: ").strip()
g = input("Número de gols: ").strip()


if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
