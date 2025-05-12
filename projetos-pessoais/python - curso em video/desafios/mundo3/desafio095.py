jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input("Nome do jogador: ")

    num_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    gols = []
    for i in range(num_partidas):
        gols.append(int(input(f"  Quantos gols na partida {i+1}? ")))

    jogador['gols'] = gols
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    continuar = input("Deseja cadastrar outro jogador? [S/N] ").strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input("Resposta inválida. Digite S ou N: ").strip().upper()
    if continuar == 'N':
        break

print("\n" + "="*50)
print("Cod  Nome            Gols              Total")
print("-"*50)
for i, j in enumerate(jogadores):
    print(f"{i:<4} {j['nome']:<15} {str(j['gols']):<18} {j['total']}")

while True:
    print("\nDigite o código do jogador para ver os detalhes (999 para sair):")
    codigo = int(input("Código: "))

    if codigo == 999:
        break
    if codigo < 0 or codigo >= len(jogadores):
        print("Código inválido. Tente novamente.")
    else:
        jogador = jogadores[codigo]
        print(f"\n-- LEVANTAMENTO DO JOGADOR {jogador['nome'].upper()} --")
        for i, g in enumerate(jogador['gols']):
            print(f"   No jogo {i+1} fez {g} gols.")

print("\nEncerrando o programa. Até logo!")
