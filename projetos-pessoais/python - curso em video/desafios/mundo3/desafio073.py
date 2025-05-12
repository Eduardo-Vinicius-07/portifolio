tabela=("Palmeiras", "Bragantino", "Flamengo", "Cruzeiro", "Fluminense", "Bahia",
    "Ceará SC", "Corinthians", "Internacional", "Atlético-MG", "São Paulo",
    "Botafogo", "Grêmio", "Vasco da Gama", "Juventude", "Mirassol",
    "Fortaleza", "EC Vitória", "Santos", "Sport Recife")
print(f"\n5 primeiros: {tabela[0:5]}")
print(f"\n4 ultimos: {tabela[19:15:-1]}")
print(f"\ntimes em ordem alfabetica: {(sorted(tabela))}")
print(f"\nPosição do Flamengo: {tabela.index('Flamengo') + 1}º lugar")

