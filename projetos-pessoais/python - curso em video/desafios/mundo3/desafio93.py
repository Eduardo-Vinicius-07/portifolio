jogador = {}

jogador['nome'] = input("Digite o nome do jogador: ")
num_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
jogador['partidas'] = num_partidas

gols_por_partida = []
total_gols = 0

for i in range(num_partidas):
    gols = int(input(f"Quantos gols o jogador fez na partida {i+1}? "))
    gols_por_partida.append(gols)
    total_gols += gols

jogador['gols'] = gols_por_partida
jogador['total'] = total_gols

print(f"\nO jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
for i in range(jogador['partidas']):
    print(f"=> Na partida {i+1}, fez {jogador['gols'][i]} gols.")

print(f"\nFoi um total de {jogador['total']} gols.")
print(f"{'=' * 30}")
